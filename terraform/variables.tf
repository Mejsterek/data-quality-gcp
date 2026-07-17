variable "project_id" {
  description = "GCP project ID that contains the BigQuery table."
  type        = string
  default     = "data-quality-gcp"
}

variable "region" {
  description = "Default GCP region for provider-managed regional resources."
  type        = string
  default     = "europe-central2"
}

variable "dataplex_location" {
  description = "Dataplex DataScan location. Use a location compatible with the BigQuery dataset."
  type        = string
  default     = "europe-central2"
}

variable "target_dataset_id" {
  description = "BigQuery dataset ID that contains the table to validate."
  type        = string
  default     = "data_quality"
}

variable "target_table_id" {
  description = "BigQuery table ID to validate."
  type        = string
  default     = "customers"
}

variable "sampling_percent" {
  description = "Percentage of rows scanned. Use 100 for a full scan."
  type        = number
  default     = 100
}
