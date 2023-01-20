variable "env" {
  default = "dev"
}

variable "deletion_protection" {
  default = "false"
}

variable "container_image" {
  type        = string
  description = "The container image to deploy to cloud run"
  nullable    = false
  default     = "us-central1-docker.pkg.dev/asl-dictionary/my-repository/backend-image:latest"
}