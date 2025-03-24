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
class PubsubEvents:
    def __init__(self, client: PublisherClient, project_id: str):
        self.__client = client
        self.__project_id = project_id

    def consume(self, topic_name: str, bulk_size: int):
        raise NotImplementedError

    def produce_bulk(
        self, topic_name: str, events: List[Event], attributes: dict = None
    ) -> int:
        """
        Produces a bulk of events to a topic.
        :param topic_name: topic name
        :param events: events to be sent in bulk
        :param attributes: extra attributes to be sent with the event
        :return:  Return 0 in case all events were successfully produced. In case of error, return the number of events that were not produced.
        """
        try:
            events = deepcopy(events)

            while events:
                event = events.pop(0)
                self.produce(topic_name, event, attributes)
            return len(events)
        except Exception as e:
            logger.error("Error while producing events: %s", e)
            return len(events)

    def produce(self, topic_name: str, event: Event, attributes: dict = None):
        """
            Produces an event to a topic.
        :param topic_name: topic name
        :param event: event to be sent
        :param attributes: extra attributes to be sent with the event
        :return:
        """
        topic_path = self.__client.topic_path(
            project=self.__project_id, topic=topic_name
        )
        data_bytes = event.model_dump_json().encode("utf-8")

        future = self.__client.publish(
            topic_path, data=data_bytes, **(attributes or {})
        )

        logger.info("Published message ID: %s", future.result())

    @staticmethod
    def create_with(config: PubsubEventsConfig):
        return PubsubEvents(client=PublisherClient(), project_id=config.project_id)
