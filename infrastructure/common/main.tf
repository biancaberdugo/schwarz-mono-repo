module "route_metrics" {
  source = "./route-metrics"

  bigquery-dataset-id-lading-layer = google_bigquery_dataset.lading-layer.dataset_id
}
