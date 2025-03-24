from typing import List

from pydantic import BaseModel

from src.api.models.dto.v1 import (
    DataResponseV1,
    EndpointSuccessResponseV1,
    NoopPaginationResponseV1,
)
from src.api.models.internal.taxi_route import TaxiRouteMetricsEvent


class TaxiRouteMetricsV1(BaseModel):
    """Taxi route metrics DTO V1"""

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

    @classmethod
    def from_internal(cls, event: TaxiRouteMetricsEvent) -> "TaxiRouteMetricsV1":
        """Converts internal event to DTO"""
        return cls(
            event_id=event.event_id,
            car_id=event.car_id,
            trip_id=event.trip_id,
            timestamp=event.timestamp,
            latitude=event.latitude,
            longitude=event.longitude,
            latitude_start=event.latitude_start,
            longitude_start=event.longitude_start,
            latitude_end=event.latitude_end,
            longitude_end=event.longitude_end,
            city_id=event.city_id,
            user_id=event.user_id,
            driver_id=event.driver_id,
        )


# DTO responses into pattern of data result and pagination
class TaxiRouteMetricSingleDataV1(DataResponseV1):
    metric: TaxiRouteMetricsV1


class TaxiRouteMetricMultiDataV1(DataResponseV1):
    metrics: List[TaxiRouteMetricsV1]


TaxiRouteMetricSingleEndpointSuccessResponseV1 = EndpointSuccessResponseV1[
    TaxiRouteMetricSingleDataV1, NoopPaginationResponseV1
]

TaxiRouteMetricMultiEndpointSuccessResponseV1 = EndpointSuccessResponseV1[
    TaxiRouteMetricMultiDataV1, NoopPaginationResponseV1
]
