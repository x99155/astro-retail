from datetime import datetime, timedelta

from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType




# Definir les paramètres de base du dag
@dag(
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "x99155", "retries": 3},
    tags=["retail"],
)
def retail(): # ceci est le dag_id


    # Cette tache télécharge le fichier csv dans cloud storage
    upload_csv_to_gcp = LocalFilesystemToGCSOperator(
        task_id="upload_csv_to_gcp",
        src="/usr/local/airflow/include/dataset/Online_Retail_utf8.csv",
        dst="raw/Online_Retail_utf8.csv", # chemin de destination dans le bucket
        bucket="online_retail_bucket1", # nom du bucket crée sur cloud storage
        gcp_conn_id="gcp", # nom donnée lors de la création du connecteur sur airflow
        mime_type="text/csv", # précise le type de fichier qui est un fichier csv ici
    )

    # Cette crée un ensemble de données nommé (retail) dans BigQuery
    create_retail_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id="create_retail_dataset",
        dataset_id="retail", # le nom qu'aura mon dataset dans bigquery
        gcp_conn_id="gcp",
    )

    # Cette tache va transferer le fichier csv du bucket gcs vers le dataset 'retail' dans bigquery en créant une table raw_invoices
    gcs_to_bigquery = aql.load_file(
        task_id="gcs_to_bigquery",
        input_file=File(
            "gs://online_retail_bucket1/raw/Online_Retail_utf8.csv",
            conn_id="gcp",
            filetype=FileType.CSV,
        ),
        output_table=Table(
            name="raw_invoices",
            conn_id="gcp",
            metadata=Metadata(schema="retail")
        ),
        use_native_support=False,
    )

retail()