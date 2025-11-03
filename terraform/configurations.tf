terraform {
  backend "gcs" {
    prefix = "cloud_run"
  }
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">=7.0.0"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = ">=7.0.0"
    }
  }
}

provider "google" {
  impersonate_service_account = var.impersonate_service_account
}

provider "google-beta" {
  impersonate_service_account = var.impersonate_service_account
}