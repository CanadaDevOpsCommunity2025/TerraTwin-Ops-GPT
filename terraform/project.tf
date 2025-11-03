data "google_project" "main" {
  project_id = var.main_project
}

resource "google_project_service" "enabled_services" {
  for_each = toset([
    "run.googleapis.com",
    "artifactregistry.googleapis.com",
    "iam.googleapis.com",
    "cloudbuild.googleapis.com",
    # "servicenetworking.googleapis.com",
    "compute.googleapis.com",
    # "vpcaccess.googleapis.com",
    "storage.googleapis.com",
    "aiplatform.googleapis.com",
  ])

  project = data.google_project.main.project_id
  service = each.key

  disable_on_destroy = false
  
}
