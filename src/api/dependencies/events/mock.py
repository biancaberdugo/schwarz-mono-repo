import logging
from copy import deepcopy
from typing import List

from google.cloud.pubsub_v1 import PublisherClient

from src.api.dependencies.events import EventsStreaming
from src.api.dependencies.utils import check_protocol
from src.api.models.internal import Event
from src.api.dependencies.config import PubsubEventsConfig

logger = logging.getLogger(__name__)


@check_protocol(EventsStreaming)
class MockEvents:
    def consume(self, topic_name: str, bulk_size: int):
        raise NotImplementedError

    def produce_bulk(
        self, topic_name: str, events: List[Event], attributes: dict = None
    ) -> int:
        logger.info(
            "Sending %s events to topic %s with attributes %s",
            len(events),
            topic_name,
            attributes,
        )
        return 0

    def produce(self, topic_name: str, event: Event, attributes: dict = None):
        logger.info(
            "Published %s to topic %s with attributes %s",
            event.model_dump_json(),
            topic_name,
            attributes,
        )

    @staticmethod
    def create_with(_):
        return MockEvents()
