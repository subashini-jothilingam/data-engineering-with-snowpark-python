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

![Architecture](https://github.com/user-attachments/assets/d92b53fd-5969-4441-a8c6-74de4e07b1c0)

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
├── .github/
│   └── workflows/
│       └── ...
│
├── images/
│   ├── *.png
│   ├── *.svg
│   └── ...
│
├── steps/
│   ├── 01_setup_snowflake.sql
│   │
│   ├── 02_load_raw.py
│   │
│   ├── 03_load_weather.sql
│   │
│   ├── 04_create_pos_view.py
│   │
│   ├── 05_fahrenheit_to_celsius_udf/
|   |   |__ fahrenheit_to_celsius_udf/
│   │       ├── function.py
│   │   ├── snowflake.yml
│   │   └── requirements.txt
│   │
│   ├── 06_orders_update_sp/
|   |   |── orders_update_sp/
│   │       ├── procedure.py
│   │   ├── snowflake.yml
│   │   └── requirements.txt
│   │
│   ├── 07_daily_city_metrics_update_sp/
|   |   |── daily_city_metrics_update_sp/
│   │       ├── procedure.py
│   │   ├── snowflake.yml
│   │   └── requirements.txt
|   │
|   ├── 08_orchestrate_jobs.sql
|   ├── 09_process_incrementally.sql
|   ├── 10_deploy_via_cicd.sql
|
├── .gitignore
├── deploy_snowpark_apps.py
├── environment.yml
├── requirements.txt
├── LICENSE
├── LEGAL.md
└── README.md
```

# Pipeline Workflow

This project demonstrates a complete Snowflake-native data engineering pipeline using **Snowpark Python**, **Python UDFs**, **Stored Procedures**, **Streams**, **Tasks**, and **GitHub Actions**.

---

## Step 1 – Snowflake Environment Setup

**Folder**

```
steps/01_setup_snowflake.sql
```

Creates the required Snowflake infrastructure.

**Objects Created**

- Database
- Schema
- Warehouse
- File Format
- Stage
- Tables
- Required permissions

---

## Step 2 – Load Raw Data

**File**

```
steps/02_load_raw.py
```

Loads raw weather and point-of-sale datasets into Snowflake.

**Highlights**

- Snowpark Python
- DataFrame API
- Bulk data loading
- Initial ingestion

---

## Step 3 – Load Weather Data

**File**

```
steps/03_load_weather.sql
```

Loads weather data into Snowflake tables using SQL.

**Responsibilities**

- Populate weather tables
- Validate imported records
- Prepare data for downstream processing

---

## Step 4 – Create POS View

**File**

```
steps/04_create_pos_view.py
```

Creates a Snowpark DataFrame-based view that joins and prepares Point-of-Sale data for analytics.

**Responsibilities**

- Data cleansing
- Column standardization
- Business transformations
- View creation

---

## Step 5 – Create Python UDF

**Folder**

```
steps/05_fahrenheit_to_celsius_udf/
```

Implements a reusable Python User Defined Function (UDF).

```
fahrenheit_to_celsius_udf/
    function.py
```

**Purpose**

Convert temperature values from Fahrenheit to Celsius within Snowflake.

**Technologies**

- Snowpark Python
- Python UDF
- SnowCLI Deployment

---

## Step 6 – Orders Update Stored Procedure

**Folder**

```
steps/06_orders_update_sp/
```

Creates a Python Stored Procedure responsible for updating order-related data.

```
orders_update_sp/
    procedure.py
```

**Responsibilities**

- Process new order records
- Execute transformation logic
- Update target tables

---

## Step 7 – Daily City Metrics Stored Procedure

**Folder**

```
steps/07_daily_city_metrics_update_sp/
```

Calculates daily city-level weather and sales metrics.

```
daily_city_metrics_update_sp/
    procedure.py
```

**Responsibilities**

- Aggregate daily metrics
- Generate city-level KPIs
- Produce analytics-ready datasets

---

## Step 8 – Orchestrate Pipeline

**File**

```
steps/08_orchestrate_jobs.sql
```

Creates Snowflake Tasks that orchestrate the execution of all pipeline components.

Pipeline execution order:

```
Load Data
      │
      ▼
Create Views
      │
      ▼
Execute UDF
      │
      ▼
Run Orders Update Procedure
      │
      ▼
Run Daily Metrics Procedure
```

---

## Step 9 – Incremental Processing

**File**

```
steps/09_process_incrementally.sql
```

Implements Change Data Capture (CDC) using Snowflake Streams.

Only newly inserted or modified records are processed.

**Benefits**

- Faster execution
- Lower compute cost
- Production-ready incremental pipeline

---

## Step 10 – CI/CD Deployment

**File**

```
steps/10_deploy_via_cicd.sql
```

Demonstrates automated deployment using SnowCLI and GitHub Actions.

Deployment workflow:

```
Developer
      │
      ▼
Git Commit
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Actions
      │
      ▼
SnowCLI
      │
      ▼
Deploy Snowpark Objects
      │
      ▼
Snowflake
```

---

# End-to-End Execution Flow

```
01_setup_snowflake.sql
            │
            ▼
02_load_raw.py
            │
            ▼
03_load_weather.sql
            │
            ▼
04_create_pos_view.py
            │
            ▼
05_fahrenheit_to_celsius_udf
            │
            ▼
06_orders_update_sp
            │
            ▼
07_daily_city_metrics_update_sp
            │
            ▼
08_orchestrate_jobs.sql
            │
            ▼
09_process_incrementally.sql
            │
            ▼
10_deploy_via_cicd.sql
            │
            ▼
Analytics & Reporting
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

## 👤 Author

**Subashini Jothilingam**

Data Engineer | Snowflake | PySpark | Airflow | dbt | AWS | SQL

GitHub: https://github.com/subashini-jothilingam
LinkedIn: https://linkedin.com/in/subashini-jothilingam
