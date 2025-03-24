from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from starlette import status

from src.api.dependencies.containers import ServiceContainer
from src.api.endpoints import RouterInfo, create_router_for_version

from src.api.models.dto.v1.trips import (
    TripResponseSingleDataV1,
    TripRequestV1,
    TripResponseSingleEndpointSuccessResponseV1,
)
from src.api.models.internal.trips import TripRequest
from src.api.services.trips import TripsService

router_info = RouterInfo(name="TripsServiceSimulation")
router_v1 = create_router_for_version(1)


@router_v1.post(
    "/trips/new",
    status_code=status.HTTP_200_OK,
    response_model=TripResponseSingleEndpointSuccessResponseV1,
)
@inject
async def simulate_new_trip_request(
    trip_request: TripRequestV1,
    trips_service: TripsService = Depends(Provide[ServiceContainer.trips_service]),
) -> TripResponseSingleDataV1:
    # TODO: here we would have the call to TripsService that it will implements the way to communicate to the
    # trips external service. This communication can be by API <> API or even by async events
    # all depends on how this Trips service can communicate.

    response = trips_service.request_trip(
        trip_request=TripRequest.from_bff_dto_v1(trip_request=trip_request)
    )

    return TripResponseSingleEndpointSuccessResponseV1(
        data=TripResponseSingleDataV1(event=response.to_bff_dto_v1())
    )
