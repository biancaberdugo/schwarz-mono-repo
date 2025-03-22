resource "google_pubsub_topic" "app-route-metrics-topic" {
  name         = "route-metrics-topic"
  kms_key_name = google_kms_crypto_key.route-metrics-crypto-key.id
}

resource "google_pubsub_subscription" "app-route-metrics-subscription" {
  name  = "route-metrics-subscription"
  topic = google_pubsub_topic.app-route-metrics-topic.id

  bigquery_config {
    table = "${google_bigquery_table.route-metrics.project}.${google_bigquery_table.route-metrics.dataset_id}.${google_bigquery_table.route-metrics.table_id}"
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
