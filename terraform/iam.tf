# main project
resource "google_service_account" "cloud_run_sa" {
  account_id   = "cloud-run-sa"
  display_name = "Cloud Run Service Account"
  project      = data.google_project.main.project_id
}

resource "google_project_iam_member" "run_aiplatform_user" {
  project = data.google_project.main.project_id
  role    = "roles/aiplatform.user"
  member  = "serviceAccount:${google_service_account.cloud_run_sa.email}"
}

resource "google_project_iam_member" "run_creator" {
  project = data.google_project.main.project_id
  role    = "roles/run.builder"
  member  = "serviceAccount:${google_service_account.cloud_run_sa.email}"
}