from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import os

AIRFLOW_HOME =  os.environ["AIRFLOW_HOME"]


with DAG(
    dag_id="dow30_pull_data",
    start_date=datetime(2024, 1, 1),
    schedule_interval="30 22 * * *",
    catchup=False
) as dag:

    hello_world = BashOperator(
        task_id="dow30_pull_data_task",
        bash_command="source /opt/airflow/dags/scripts/pull_data.sh ",
    )
