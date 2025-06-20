provider "google" {
  project = var.project
  region  = "us-central1"
}

resource "google_storage_bucket" "my_bucket" {
  name     = "${replace(var.project, "_", "-")}-bucket-demo"
  location = "US"
}

variable "project" {
  description = "rare-highway-461609-k2"
  type        = string
}

