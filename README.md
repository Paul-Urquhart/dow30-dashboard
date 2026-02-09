# Dow Jones Pipeline Output — Streamlit on VPS
This repository contains the serving layer of an end‑to‑end data engineering project. Daily Dow Jones Industrial Average (DJIA) data is ingested from the Yahoo Finance API into a Databricks pipeline, where it is cleaned, transformed, de‑duplicated, and stored. The processed data is then transferred to a VPS and exposed publicly through a lightweight Streamlit dashboard.

Note: This repository is one half of a two‑component project. The complementary repository containing the Databricks ingestion and transformation pipeline can be found 

Link to Databricks repository: https://github.com/Paul-Urquhart/dow30-databricks


## Architecture Diagram

```
dow30-vps/
├── airflow/
│   └── dags/
│       └── dow30_pull_data_dag.py
├── scripts/
│   └── pull_data.sh
├── app.py
├── README.md
```



## Data Transfer
Processed data is stored in Databricks as CSV files. A daily shell script running on the VPS retrieves the latest files and places them into the local data directory.
The script is scheduled to run 15 minutes after the Databricks job completes, providing a buffer for job duration and any automatic retries.

## Orchestration — Cron vs Airflow
Although the data only updates once per day and could be handled with a simple cron job, this project uses Airflow to orchestrate the transfer.
This choice provides hands‑on experience with Airflow DAGs, scheduling, and task management while keeping the workflow intentionally minimal.

## Serving Layer
The dashboard presents:
- An OHLC chart of the DJIA for the last 30 trading days
- A 20‑day moving average
- Tables showing the top and bottom performers from the previous trading day
The application is built with Streamlit, which provides a powerful yet lightweight framework for creating interactive data applications in pure Python. The dashboard is hosted on a VPS and served to the internet behind Nginx.
