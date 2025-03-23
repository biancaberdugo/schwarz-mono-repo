from typing import runtime_checkable, Protocol, List

from src.api.models.internal import Event
from src.api.dependencies.config import EventsBaseConfig


@runtime_checkable
class EventsStreaming(Protocol):
    def consume(self, topic_name: str, bulk_size: int): ...

    def produce(self, topic_name: str, event: Event, attributes: dict = None): ...

    def produce_bulk(
        self, topic_name: str, events: List[Event], attributes: dict = None
    ): ...

    @staticmethod
    def create_with(config: EventsBaseConfig): ...
