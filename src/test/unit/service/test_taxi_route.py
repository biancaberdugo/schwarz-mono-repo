from src.api.models.internal.taxi_route import (
    TaxiRouteMetricsEvents,
)
from src.api.services.taxi_route_service import TaxiRouteService


def test_taxi_metrics_route_mocked_pubsub(taxi_route_service: TaxiRouteService):
    # TODO this test is a bit useless because the method send_simulated_events
    # just send the events and this one is Mocked
    # Works better for validating service methods routines by just mocking the external dependencies
    # facilitating the validation of business logic only

    taxi_events_holder = TaxiRouteMetricsEvents.from_json_path(
        path_from_src=f"simulation/GPS_Car_Trip_Simulation_small_set_events.json"
    )
    events_left = taxi_route_service.send_simulated_events(
        route_events=taxi_events_holder.events
    )

    assert events_left == 0
