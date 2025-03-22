resource "google_service_account" "gke-bff-api-svc-account" {
  account_id   = "gke-svc-account"
  display_name = "GKE svc"
}

resource "google_container_cluster" "gke-bff-cluster" {
  name               = "bff-ccluster"
  location           = var.zone
  initial_node_count = 3
  node_config {
    service_account = google_service_account.gke-bff-api-svc-account.email
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
  timeouts {
    create = "30m"
    update = "40m"
  }
}