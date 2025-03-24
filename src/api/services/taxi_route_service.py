from typing import List

from src.api.dependencies.config import EventsBaseConfig
from src.api.dependencies.events import EventsStreaming
from src.api.models.internal.taxi_route import TaxiRouteMetricsEvent


class TaxiRouteService:

    def __init__(
        self, events_streaming: EventsStreaming, events_config: EventsBaseConfig
    ):
        self.__events_streaming = events_streaming
        self.__events_config = events_config

    def send_simulated_events(self, route_events: List[TaxiRouteMetricsEvent]) -> int:
        """
            Send the simulated events to the events streaming service.
        :param route_events: events from taxi metrics to be sent
        :return: amount of events left behind. in case of success, it should be 0 events left behind.
        """
        events_left_behind = self.__events_streaming.produce_bulk(
            topic_name=self.__events_config.taxi_route_topic_id,
            events=route_events,
        )

        return events_left_behind
