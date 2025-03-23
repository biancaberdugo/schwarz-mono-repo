from src.test.it.helpers import post_send_simulate_metrics_taxi_coordinates


from src.api.models.dto.v1.taxi_route import (
    TaxiRouteMetricMultiEndpointSuccessResponseV1,
)


def test_simulate_metrics_v1(app_client):
    result = post_send_simulate_metrics_taxi_coordinates(client=app_client)

    assert result.status_code == 200
    data = TaxiRouteMetricMultiEndpointSuccessResponseV1.model_validate(result.json())

    assert data
