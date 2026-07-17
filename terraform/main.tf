locals {
  target_table_resource = "//bigquery.googleapis.com/projects/${var.project_id}/datasets/${var.target_dataset_id}/tables/${var.target_table_id}"
}

resource "google_project_service" "required" {
  for_each = toset([
    "bigquery.googleapis.com",
    "dataplex.googleapis.com",
  ])

  project = var.project_id
  service = each.value

  disable_on_destroy = false
}

resource "google_dataplex_datascan" "customers_quality" {
  project      = var.project_id
  location     = var.dataplex_location
  data_scan_id = "customers-quality"
  display_name = "Customers data quality"
  description  = "Data quality rules for ${var.target_dataset_id}.${var.target_table_id}."

  data {
    resource = local.target_table_resource
  }

  execution_spec {
    trigger {
      on_demand {}
    }
  }

  data_quality_spec {
    sampling_percent            = var.sampling_percent

    rules {
      name      = "table-not-empty"
      dimension = "COMPLETENESS"

      table_condition_expectation {
        sql_expression = "COUNT(*) > 0"
      }
    }

    rules {
      name      = "name-required"
      column    = "name"
      dimension = "COMPLETENESS"
      threshold = 1

      non_null_expectation {}
    }

    rules {
      name      = "id-unique"
      column    = "id"
      dimension = "UNIQUENESS"
      threshold = 1

      uniqueness_expectation {}
    }

    rules {
      name      = "age-valid-range"
      column    = "age"
      dimension = "VALIDITY"
      threshold = 1

      range_expectation {
        min_value = 0
        max_value = 120
      }
    }

    rules {
      name      = "email-valid-format"
      column    = "email"
      dimension = "VALIDITY"
      threshold = 1

      regex_expectation {
        regex = "^[\\w.\\-]+@[\\w.\\-]+\\.[A-Za-z]+$"
      }
    }
  }

  labels = {
    app = "data-quality"
  }

  depends_on = [
    google_project_service.required,
  ]
}
