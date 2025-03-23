from dataclasses import dataclass
from typing import Type

from dependency_injector import containers, providers

from src.api.dependencies.events import EventsStreaming
from src.api.dependencies.config import (
    AppConfig,
    EventsStreamingType,
    EventsBaseConfig,
    PubsubEventsConfig,
    MockEventsConfig,
)

from src.api.services.taxi_route_service import TaxiRouteService


def get_config() -> AppConfig:
    container = AppContainer()

    config = container.config()

    return AppConfig.model_validate(config)


@dataclass
class ServicesDependencies:
    events_streaming: Type[EventsStreaming]
    events_config: Type[EventsBaseConfig]


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration(pydantic_settings=[AppConfig()])


def get_external_dependencies() -> ServicesDependencies:
    config: AppConfig = get_config()

    if config.events_streaming_type == EventsStreamingType.PUBSUB:
        from src.api.dependencies.events.pubsub_events import PubsubEvents

        events_streaming = PubsubEvents
        events_config = PubsubEventsConfig
    elif config.events_streaming_type == EventsStreamingType.KAFKA:
        raise NotImplementedError("Kafka is not implemented yet")
    elif config.events_streaming_type == EventsStreamingType.MOCK:
        from src.api.dependencies.events.mock import MockEvents

        events_streaming = MockEvents
        events_config = MockEventsConfig

    return ServicesDependencies(
        events_streaming=events_streaming, events_config=events_config
    )


class ExternalDependenciesContainer(containers.DeclarativeContainer):
    external_dependencies = providers.Singleton(get_external_dependencies)

    events_config = providers.Singleton(external_dependencies.provided.events_config())

    events_streaming: EventsStreaming = providers.Factory(
        external_dependencies.provided.events_streaming.create_with(), events_config()
    )


class ServiceContainer(containers.DeclarativeContainer):
    __external_dependencies = providers.Container(ExternalDependenciesContainer)

    taxi_route_service = providers.Factory(
        TaxiRouteService,
        events_streaming=__external_dependencies.events_streaming,
        events_config=__external_dependencies.events_config,
    )
