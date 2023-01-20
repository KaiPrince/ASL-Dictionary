resource "google_compute_network" "vpc_network" {
  name                    = "terraform-network"
  auto_create_subnetworks = "true"
}

#resource "google_vpc_access_connector" "connector" {
#  name          = "vpc-con"
#  ip_cidr_range = "10.8.0.0/28"
#  network       = google_compute_network.vpc_network.self_link
#}