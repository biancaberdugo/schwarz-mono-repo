import json
from enum import StrEnum
from pathlib import Path
from typing import List

from src.api.models.internal import Event

BASE_PATH = Path(__file__).parent.parent.parent.parent


class SimulationFiles(StrEnum):
    GPS_Car_Trip_Simulation_large_5k_events = "GPS_Car_Trip_Simulation_large_5k_events"
    GPS_Car_Trip_Simulation_small_set_events = (
        "GPS_Car_Trip_Simulation_small_set_events"
    )


class TaxiRouteMetricsEvent(Event):
    """Taxi route metrics model."""

    event_id: str
    car_id: str
    trip_id: str
    timestamp: float
    latitude: float
    longitude: float
    latitude_start: float
    longitude_start: float
    latitude_end: float
    longitude_end: float
    city_id: int
    user_id: str
    driver_id: str


class TaxiRouteMetricsEvents(Event):
    events: List[TaxiRouteMetricsEvent]

    @classmethod
    def from_json_path(cls, path_from_src: str) -> "TaxiRouteMetricsEvents":
        path = BASE_PATH / path_from_src

        with open(path, "r") as f:
            events = [
                TaxiRouteMetricsEvent.model_validate(json.loads(line))
                for line in f
                if line.strip()
            ]

        return cls(events=events)

    def amount_of_events(self):
        return len(self.events)
