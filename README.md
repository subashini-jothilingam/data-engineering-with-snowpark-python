# End-to-End Data Engineering Pipeline with Snowpark Python & Snowflake

![Snowflake](https://img.shields.io/badge/Snowflake-Cloud-blue)
![Python](https://img.shields.io/badge/Python-3.11-yellow)
![Snowpark](https://img.shields.io/badge/Snowpark-Python-green)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Overview

This project demonstrates how to build a **production-ready data engineering pipeline** entirely within **Snowflake** using **Snowpark Python**.

Instead of relying on multiple external orchestration and compute platforms, this solution leverages Snowflake's native capabilities for:

- Data ingestion
- Incremental processing
- Python-based transformations
- Change Data Capture (CDC)
- Pipeline orchestration
- Monitoring
- CI/CD deployment

The project follows modern cloud data engineering best practices and showcases how enterprise data platforms can be developed using Snowpark Python.

---

# Architecture

![Architecture](docs/architecture.png)

## Architecture Flow

```
                  Source Files (Parquet)
                          │
                          ▼
                COPY INTO (Bronze Layer)
                          │
                          ▼
                Raw Snowflake Tables
                          │
                          ▼
                 Streams (CDC Tracking)
                          │
                          ▼
           Snowpark Python Transformations
                          │
          ┌───────────────┴───────────────┐
          │                               │
     Python UDFs                  Business Logic
          │                               │
          └───────────────┬───────────────┘
                          ▼
                 Curated Gold Tables
                          │
                          ▼
                BI / Analytics / ML
                          ▲
                          │
           Tasks + Stored Procedures
                          │
                          ▼
              Automated Pipeline Execution

Developer
    │
GitHub
    │
GitHub Actions
    │
SnowCLI
    │
Snowflake Deployment
```

---

# Technology Stack

| Technology | Purpose |
|------------|----------|
| Snowflake | Cloud Data Warehouse |
| Snowpark Python | Data Transformation |
| Python | Business Logic |
| SQL | Data Manipulation |
| Streams | Change Data Capture |
| Tasks | Scheduling |
| Stored Procedures | Pipeline Orchestration |
| COPY INTO | Data Loading |
| Parquet | Source Data |
| GitHub | Version Control |
| GitHub Actions | CI/CD |
| SnowCLI | Deployment |

---

# Project Structure

```
snowpark-data-engineering-pipeline/

│
├── data/
│   ├── raw/
│   └── sample_data/
│
├── sql/
│   ├── create_tables.sql
│   ├── create_streams.sql
│   ├── create_tasks.sql
│   └── create_procedures.sql
│
├── python/
│   ├── transformations.py
│   ├── udf.py
│   ├── stored_procedures.py
│   └── pipeline.py
│
├── deployment/
│   ├── snowcli.yml
│   └── deploy.sql
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── docs/
│   └── architecture.png
│
└── README.md
```

---

# Pipeline Workflow

## Step 1 — Data Ingestion

Source data is stored as Parquet files.

```
Parquet Files
      │
COPY INTO
      │
Bronze Tables
```

Features:

- Auto schema inference
- High-performance bulk loading
- Native Snowflake ingestion

---

## Step 2 — Incremental Processing

Instead of scanning the full dataset every run, Snowflake Streams capture:

- Inserts
- Updates
- Deletes

Only changed records are processed.

Benefits:

- Lower compute cost
- Faster execution
- Production scalability

---

## Step 3 — Data Transformation

Transformations are implemented using the Snowpark DataFrame API.

Example operations:

- Data cleansing
- Standardization
- Deduplication
- Filtering
- Aggregations
- Joins
- Window functions

---

## Step 4 — Python UDFs

Reusable business logic is implemented as Python UDFs.

Example:

- Customer segmentation
- Risk scoring
- Data validation
- Standardized calculations

---

## Step 5 — Stored Procedures

Python Stored Procedures orchestrate the entire pipeline.

Responsibilities:

- Execute transformations
- Handle errors
- Maintain execution order
- Log execution status

---

## Step 6 — Scheduling

Snowflake Tasks automate pipeline execution.

Example schedule:

```
Every Hour
      │
      ▼
Call Stored Procedure
      │
Execute Pipeline
      │
Update Gold Tables
```

---

## Step 7 — Monitoring

Pipeline health can be monitored using:

- Task History
- Query History
- Execution Logs
- Snowsight Dashboard

---

## Step 8 — CI/CD

Deployment pipeline:

```
Developer
     │
Git Commit
     │
GitHub
     │
GitHub Actions
     │
SnowCLI
     │
Deploy to Snowflake
```

Pipeline validates:

- SQL
- Python
- Objects
- Deployment scripts

before deployment.

---

# Key Snowflake Features Used

✔ COPY INTO

✔ Snowpark Python

✔ DataFrame API

✔ Python UDFs

✔ Stored Procedures

✔ Streams

✔ Tasks

✔ Snowsight

✔ SnowCLI

---

# Business Benefits

- Fully managed cloud-native pipeline
- Incremental processing
- Minimal data movement
- Native Python transformations
- Automated scheduling
- CI/CD enabled
- Scalable architecture
- Enterprise-ready deployment
- Lower operational overhead
- Cost-efficient processing

---

# Skills Demonstrated

- Snowflake
- Snowpark Python
- Python
- SQL
- Data Engineering
- Change Data Capture (CDC)
- Cloud Data Platforms
- ETL / ELT
- Data Pipelines
- GitHub Actions
- CI/CD
- Cloud Architecture

---

# Future Enhancements

- Integrate dbt transformations
- Add data quality testing
- Implement Snowflake Dynamic Tables
- Add Snowpipe Streaming
- Metadata-driven ingestion
- Data lineage
- Slack/Teams pipeline notifications
- Great Expectations integration

---

# References

- Snowflake Snowpark Python
- Snowflake Streams
- Snowflake Tasks
- SnowCLI
- GitHub Actions

---

# Author

**Subashini**

Senior Data Engineer

**Core Skills**

- Snowflake
- Snowpark Python
- SQL
- Python
- AWS
- Airflow
- dbt
- Data Warehousing
- ETL / ELT
- Cloud Data Engineering

---

## If you found this project helpful, consider giving it a ⭐ on GitHub.
