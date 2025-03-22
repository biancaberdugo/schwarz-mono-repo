variable "env" {
  type        = string
  description = "The environment name, e.g. dev, prod, etc."
}

variable "owner" {
  default = "data-platform"
  type    = string
}

variable "project_id" {
  default = "GCP project id"
  type    = string
}

variable "region" {
  type        = string
  description = "GCP Region"
  default     = "us-central1"
}

variable "zone" {
  type        = string
  description = "GCP Zone"
  default     = "us-central1-c"
}