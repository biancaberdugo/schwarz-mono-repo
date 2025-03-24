# Ideally the DTOs should be an external library just for reusing it in all the places that communicates within the endpoint
# It is easier to bump DTOs all over the usages if it is just a matter of downloading it from a lib
from typing import List

from pydantic import BaseModel

from src.api.models.dto.v1 import (
    DataResponseV1,
    EndpointSuccessResponseV1,
    NoopPaginationResponseV1,
)


class TripRequestV1(BaseModel):
    event_id: str
    user_id: str
    longitude_start: float
    longitude_end: float
    latitude_start: float
    latitude_end: float


class TripResponseV1(BaseModel):
    event_id: str
    user_id: str
    driver_id: str


# TripResponse
class TripResponseSingleDataV1(DataResponseV1):
    event: TripResponseV1


class TripResponseMultiDataV1(DataResponseV1):
    event: List[TripResponseV1]


TripResponseSingleEndpointSuccessResponseV1 = EndpointSuccessResponseV1[
    TripResponseSingleDataV1, NoopPaginationResponseV1
]

TripResponseMultiEndpointSuccessResponseV1 = EndpointSuccessResponseV1[
    TripResponseMultiDataV1, NoopPaginationResponseV1
]
