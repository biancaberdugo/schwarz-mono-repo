resource "google_pubsub_schema" "app-route-metrics-topic-schema" {
  name       = "gps-car-trip-simulation-schema"
  type       = "AVRO"
  definition = <<EOF
{
  "type": "record",
  "name": "GPSCarTripSimulation",
  "namespace": "com.example.avro",
  "fields": [
    {"name": "event_id",         "type": "string"},
    {"name": "car_id",           "type": "string"},
    {"name": "trip_id",          "type": "string"},
    {"name": "timestamp",        "type": "double"},
    {"name": "latitude",         "type": "double"},
    {"name": "longitude",        "type": "double"},
    {"name": "latitude_start",   "type": "double"},
    {"name": "longitude_start",  "type": "double"},
    {"name": "latitude_end",     "type": "double"},
    {"name": "longitude_end",    "type": "double"},
    {"name": "city_id",          "type": "int"},
    {"name": "user_id",          "type": "string"},
    {"name": "driver_id",        "type": "string"}
  ]
}
EOF
}


resource "google_pubsub_topic" "app-route-metrics-topic" {
  name         = "route-metrics-topic"
  kms_key_name = google_kms_crypto_key.route-metrics-crypto-key.id

  depends_on = [google_pubsub_schema.app-route-metrics-topic-schema]
  schema_settings {
    schema   = google_pubsub_schema.app-route-metrics-topic-schema.id
    encoding = "JSON"
  }
}


resource "google_pubsub_topic" "app-route-dead-letter-topic" {
  name = "route-dead-letter-topic"
}

resource "google_pubsub_subscription" "app-route-metrics-subscription" {
  name  = "route-metrics-subscription"
  topic = google_pubsub_topic.app-route-metrics-topic.id

  bigquery_config {
    table               = "${google_bigquery_table.route-metrics.project}.${google_bigquery_table.route-metrics.dataset_id}.${google_bigquery_table.route-metrics.table_id}"
    use_topic_schema    = true
    drop_unknown_fields = true
  }

  dead_letter_policy {
    dead_letter_topic     = google_pubsub_topic.app-route-dead-letter-topic.id
    max_delivery_attempts = 10
  }
}

resource "google_kms_key_ring" "route-metrics-key-ring" {
  name     = "pubsub-route-metrics-keyring"
  location = "global"
}

resource "google_kms_crypto_key" "route-metrics-crypto-key" {
  name     = "pubsub-route-metrics-key"
  key_ring = google_kms_key_ring.route-metrics-key-ring.id
}

resource "google_kms_crypto_key_iam_binding" "pubsub_crypto_key_binding" {
  crypto_key_id = google_kms_crypto_key.route-metrics-crypto-key.id
  role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
  members = [
    "serviceAccount:service-293693980551@gcp-sa-pubsub.iam.gserviceaccount.com",
  ]
}
