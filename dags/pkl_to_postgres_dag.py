from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='pkl_to_postgres_dag',
    schedule_interval=None,
    default_args=default_args,
    tags=['etl', 'pkl'],
    description='load pickles to postgres'
) as dag:

    run_ingestion = BashOperator(
        task_id='run_pkl_to_postgres',
        bash_command='python /opt/airflow/scripts/pkl_to_postgres.py'
    )
