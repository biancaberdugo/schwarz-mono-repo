from dependency_injector.wiring import inject, Provide
from fastapi import Depends, Query
from starlette import status

from src.api.dependencies.containers import ServiceContainer
from src.api.endpoints import RouterInfo, create_router_for_version
from src.api.models.dto.v1.taxi_route import (
    TaxiRouteMetricsV1,
    TaxiRouteMetricMultiEndpointSuccessResponseV1,
    TaxiRouteMetricMultiDataV1,
)
from src.api.models.internal.taxi_route import TaxiRouteMetricsEvents, SimulationFiles
from src.api.services.taxi_route_service import TaxiRouteService

router_info = RouterInfo(name="SimulateEvents")
router_v1 = create_router_for_version(1)


@router_v1.post(
    "/simulate-events/taxi-route/trip-coordinates/",
    status_code=status.HTTP_200_OK,
    response_model=TaxiRouteMetricMultiEndpointSuccessResponseV1,
)
@inject
async def send_simulate_metrics_taxi_coordinates(
    simulation_name: SimulationFiles = Query(
        alias="simulation_name",
        default="GPS_Car_Trip_Simulation_small_set_events",
        description="The name of the simulation to be sent.",
    ),
    taxi_route_service: TaxiRouteService = Depends(
        Provide[ServiceContainer.taxi_route_service]
    ),
) -> TaxiRouteMetricMultiEndpointSuccessResponseV1:
    taxi_events_holder = TaxiRouteMetricsEvents.from_json_path(
        path_from_src=f"simulation/{simulation_name}.json"
    )
    events_left = taxi_route_service.send_simulated_events(
        route_events=taxi_events_holder.events
    )

    return TaxiRouteMetricMultiEndpointSuccessResponseV1(
        data=TaxiRouteMetricMultiDataV1(
            metrics=[
                TaxiRouteMetricsV1.from_internal(event)
                for event in taxi_events_holder.events
            ]
        ),
        metadata={
            "simulation_name": simulation_name,
            "events_left_behind": str(events_left),
            "events_sent": str(taxi_events_holder.amount_of_events()),
        },
    )
