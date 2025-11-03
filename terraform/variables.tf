variable "backend_bucket" {
  description = "backend bucket for terraform state"
  type = string
}

variable "impersonate_service_account" {
  description = "Service account used for service account impersonation"
  type = string
}

variable "main_project" {
  description = "target project for terraform deployments"
  type = string
}

variable "region" {
  description = "GCP Region"
  type = string
  default = "us-central1"
}