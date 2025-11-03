resource "google_cloud_run_v2_service" "root_agent" {
  name = "root-agent"
  location = var.region
  project = data.google_project.main.project_id
  description = "Cloud Run service for Root Agent"
  scaling {
    min_instance_count = 1
    max_instance_count = 2
  }
  traffic {
    type = "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"
    percent = 100
  }
  template {

      containers {
        image = "${google_artifact_registry_repository.cloud-run-source-deploy.registry_uri}/test-agent:latest"
        env {
          name  = "GOOGLE_CLOUD_PROJECT"
          value = data.google_project.main.project_id
        }
        env {
          name  = "GOOGLE_CLOUD_LOCATION"
          value = var.region
        }
        env {
          name  = "GOOGLE_GENAI_USE_VERTEXAI"
          value = "1"
        }
      }
      service_account = google_service_account.cloud_run_sa.email
    }
  }

data "google_iam_policy" "run_instance_access" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_v2_service_iam_policy" "policy" {
  project = data.google_project.main.project_id
  location = var.region
  name = google_cloud_run_v2_service.root_agent.name
  policy_data = data.google_iam_policy.run_instance_access.policy_data
}