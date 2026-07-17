output "datascan_name" {
  description = "Full Dataplex DataScan resource name."
  value       = google_dataplex_datascan.customers_quality.name
}

output "target_table_resource" {
  description = "BigQuery table resource scanned by Dataplex."
  value       = local.target_table_resource
}
