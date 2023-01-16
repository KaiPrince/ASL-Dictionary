provider "google" {
  project = "asl-dictionary"
  region  = "us-central1"
  zone    = "us-central1-c"
}

locals {
  env = "dev"
}

module "compute" {
  source = "../../modules/compute"

  network = module.vpc.network
}

module "vpc" {
  source = "../../modules/vpc"
}

module "base_config" {
  source = "../base"
}