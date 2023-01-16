provider "google" {
  project = module.base_config.project_name
  region  = module.base_config.region
  zone    = module.base_config.zone
}

module "container_registry" {
  source = "../../modules/container_registry"

  location = module.base_config.region
}

module "database" {
  source = "../../modules/database"

  region = module.base_config.region
  deletion_protection = var.deletion_protection
}

module "vpc" {
  source = "../../modules/vpc"
}

module "base_config" {
  source = "../base"
}