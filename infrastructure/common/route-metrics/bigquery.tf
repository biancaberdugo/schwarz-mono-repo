resource "google_bigquery_table" "route-metrics" {
  table_id   = "route-metrics"
  dataset_id = var.bigquery-dataset-id-lading-layer

  schema = <<EOF
[
  {
    "name": "data",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The data"
  }
]
EOF

  deletion_protection = false
}