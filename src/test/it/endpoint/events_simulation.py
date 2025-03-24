from src.test.it.helpers import post_send_simulate_metrics_taxi_coordinates


from src.api.models.dto.v1.taxi_route import (
    TaxiRouteMetricMultiEndpointSuccessResponseV1,
)

# This class shows how can we simulate the calls to the endpoints to execute e2e tests with API
# Simulating real calls to our endpoints
# TODO: replace the staging configuration for instead of using real pubsub to use the mocked version
# Or consider something such as localstack gcp equivalent


def test_simulate_metrics_v1(app_client):
    result = post_send_simulate_metrics_taxi_coordinates(client=app_client)

    assert result.status_code == 200

    # Validate if the response have the expected result
    data = TaxiRouteMetricMultiEndpointSuccessResponseV1.model_validate(result.json())

    assert data.metadata.get("events_sent") == 320
