# Data Quality API

A simple Data Quality API built with Python and Flask, containerized with Docker and ready to be deployed to Google Cloud Run.
A production-like Data Quality microservice deployed on Google Cloud Run with CI-ready architecture.

## Features

* Validate CSV datasets
* Detect missing values
* Detect duplicate IDs
* Validate email format
* Validate age range (0-120)
* Return validation results as JSON

## Tech Stack

* Python
* Flask
* Pandas
* Pytest
* Docker
* Google Cloud Run
* Artifact Registry
* Git

## Architecture

```text
User
  |
  v
Flask API (Cloud Run)
  |
  v
Pandas validation engine
  |
  v
JSON response
```

## Project Structure

```text
data-quality-gcp/
+-- app/
|   +-- main.py
|   +-- validator.py
+-- data/
|   +-- sample.csv
+-- tests/
|   +-- test_validator.py
+-- Dockerfile
+-- requirements.txt
+-- README.md
```

## Running Locally

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/main.py
```

The API will be available at:

```text
http://localhost:8080
```

Validation endpoint:

```text
http://localhost:8080/validate
```

## Running with Docker

Build the image:

```bash
docker build -t data-quality-gcp .
```

Run the container:

```bash
docker run -p 8080:8080 data-quality-gcp
```

## API Endpoints

### Health Check

```http
GET /
```

Response:

```text
Data Quality API is running
```

### Validate CSV File

```http
POST /validate
```

## How to Use API

Send a CSV file to the validation endpoint:

```bash
curl -X POST http://localhost:8080/validate \
  -F "file=@data/sample.csv"
```

Example response:

```json
{
  "missing": {
    "id": 0,
    "name": 1,
    "email": 0,
    "age": 0
  },
  "duplicate_ids": 1,
  "invalid_emails": 1,
  "invalid_ages": 2
}
```

## Deployment

The application is deployed on Google Cloud Run.

Live endpoint:

```text
https://data-quality-api-74415612191.europe-central2.run.app
```

## Testing

Run all tests:

```bash
pytest
```

## Future Improvements

* Upload CSV files through the API
* Read datasets from Google Cloud Storage
* GitHub Actions CI/CD
* Workload Identity Federation authentication
* Additional validation rules
