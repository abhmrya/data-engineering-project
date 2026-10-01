# Data Engineering Pipeline

End-to-end industry-style Data Engineering project.

## Goals

- Data ingestion
- Data formatting
- Data validation
- ETL
- ELT
- PostgreSQL
- Parquet
- Docker
- Airflow
- AWS
- CI/CD
- Monitoring
- Testing
- Data quality

## Architecture

API / CSV / JSON
        ↓
   Ingestion
        ↓
    Raw Data
        ↓
 Validation
        ↓
Transformation
        ↓
 ETL / ELT
        ↓
 PostgreSQL / S3
        ↓
 Analytics













data-engineering-project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
│
├── src/
│   ├── ingestion/
│   ├── formatting/
│   ├── validation/
│   ├── transformation/
│   ├── etl/
│   ├── elt/
│   └── database/
│
├── tests/
│
├── config/
│
├── scripts/
│
├── logs/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── main.py