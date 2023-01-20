resource "google_cloud_run_v2_service" "default" {
  name     = "cloudrun-service"
  location = var.location

  template {
    containers {
      image = var.container_image

      env {
        name = "FOO"
        value = "bar"
      }

      volume_mounts {
        name = "cloudsql"
        mount_path = "/cloudsql"
      }
    }
    scaling {
      max_instance_count = 2
    }

    volumes {
      name = "cloudsql"
      cloud_sql_instance {
        instances = ["${var.project}:${var.location}:${var.database_instance}"]
      }
    }

  }
}
