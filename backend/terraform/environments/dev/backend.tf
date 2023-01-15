terraform {
  backend "gcs" {
    bucket = "tfstate-a7e1c82f"
    prefix = "env/dev"
  }
}