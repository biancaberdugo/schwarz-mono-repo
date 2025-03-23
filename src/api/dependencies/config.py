from enum import StrEnum
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EventsStreamingType(StrEnum):
    PUBSUB: Literal["PUBSUB"] = "PUBSUB"
    KAFKA: Literal["KAFKA"] = "KAFKA"


class EventsBaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__", extra="allow")
    type: EventsStreamingType

    taxi_route_topic_id: str = Field(validation_alias="TAXI_ROUTE_TOPIC_ID")


class PubsubEventsConfig(EventsBaseConfig):
    model_config = SettingsConfigDict(env_nested_delimiter="__", extra="allow")

    project_id: str = Field(validation_alias="PUBSUB__PROJECT_ID")
    type: EventsStreamingType = EventsStreamingType.PUBSUB


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__", extra="allow")

    env: str = Field(validation_alias="ENV")
    cloud: str = Field(validation_alias="CLOUD")
    version: str = Field(validation_alias="VERSION")
    service: str = Field(validation_alias="SERVICE")
    team: str = Field(validation_alias="TEAM")

    events_streaming_type: EventsStreamingType = Field(
        validation_alias="EVENTS_STREAMING_TYPE"
    )
