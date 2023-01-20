resource "google_sql_database" "database" {
  name     = "my-database"
  instance = google_sql_database_instance.instance.name
}

# See versions at https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#database_version
resource "google_sql_database_instance" "instance" {
  name             = "my-database-instance"
  region           = var.region
  database_version = "POSTGRES_14"
  settings {
    tier = "db-f1-micro"
#    connector_enforcement = "REQUIRED"
    disk_autoresize_limit = 20
    pricing_plan = "PER_USE"
#    ip_configuration {
#      ipv4_enabled = true
#      private_network = var.network
#    }
  }

  deletion_protection  = var.deletion_protection
}