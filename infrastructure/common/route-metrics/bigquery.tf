resource "google_bigquery_table" "route-metrics" {
  table_id   = "route_metrics"
  dataset_id = var.bigquery-dataset-id-lading-layer

  schema = <<EOF
[
  {"name": "event_id",         "type": "STRING",  "mode": "NULLABLE"},
  {"name": "car_id",           "type": "STRING",  "mode": "NULLABLE"},
  {"name": "trip_id",          "type": "STRING",  "mode": "NULLABLE"},
  {"name": "timestamp",        "type": "FLOAT",   "mode": "NULLABLE"},
  {"name": "latitude",         "type": "FLOAT",   "mode": "NULLABLE"},
  {"name": "longitude",        "type": "FLOAT",   "mode": "NULLABLE"},
  {"name": "latitude_start",   "type": "FLOAT",   "mode": "NULLABLE"},
  {"name": "longitude_start",  "type": "FLOAT",   "mode": "NULLABLE"},
  {"name": "latitude_end",     "type": "FLOAT",   "mode": "NULLABLE"},
  {"name": "longitude_end",    "type": "FLOAT",   "mode": "NULLABLE"},
  {"name": "city_id",          "type": "INTEGER", "mode": "NULLABLE"},
  {"name": "user_id",          "type": "STRING",  "mode": "NULLABLE"},
  {"name": "driver_id",        "type": "STRING",  "mode": "NULLABLE"}
]
EOF

  deletion_protection = false
}