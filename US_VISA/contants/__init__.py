import os
from datetime import date
from datetime import datetime
DATABASE_NAME = "US"
COLLECTION_NAME = "visadata"
MONGODB_URL_KEY = "MONOGODB_URL"

PIPELINE_NAME :str = "usvisa"


ARTIFACT_DIR:str = "artifact"
FILE_NAME:str = "EasyVisa.csv"
MODEL_FILE_NAME = "model.pkl"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

TARGET_COLUMN:str = "case_status"
CURRRNT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME

"""
DATA_INGESTION_COLLECTION_NAME:str = "visadata"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2


"""
Data Validations related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = "report.yaml"










