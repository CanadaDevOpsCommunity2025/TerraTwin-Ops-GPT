import {
  id = "projects/${data.google_project.main.project_id}/locations/${var.region}/repositories/cloud-run-source-deploy"
  to = google_artifact_registry_repository.cloud-run-source-deploy
}

resource "google_artifact_registry_repository" "cloud-run-source-deploy" {
  project = data.google_project.main.project_id
  location = var.region
  repository_id = "cloud-run-source-deploy"
  format = "DOCKER"
}