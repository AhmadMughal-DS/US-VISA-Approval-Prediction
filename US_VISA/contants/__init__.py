import os
from datetime import datetime
DATABSE_NAME = "US"
COLLECTION_NAME = "visadata"
MONGODB_URL_KEY = "mongodb+srv://ahmadzafar:mlopsusvisa@cluster0.lnbjt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

PIPELINE_NAME :str = "usvisa"


ARTIFACT_DIR:str = "artifact"
FILE_NAME:str = "EasyVisa.csv"
MODEL_FILE_NAME = "model.pkl"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME

"""
DATA_INGESTION_COLLECTION_NAME:str = "visadata"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2







