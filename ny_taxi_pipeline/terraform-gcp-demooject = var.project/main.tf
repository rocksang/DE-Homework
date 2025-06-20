provider "google" {
  project = var.project
  region  = "us-central1"
}

resource "google_storage_bucket" "my_bucket" {
  name     = "${var.project}-bucket-demo"
  location = "US"
}

variable "project" {
  description = "Your GCP project ID"
  type        = string
}
