from os import getenv
from boto3 import client
from data_access.data_stores.sql.connection_manager import ConnectionManager
from data_access.data_stores.sql.repositories.read import ReadRepository
from data_access.data_stores.sql.query_handlers.ml_model_data import MLModelQueryHandler
from data_access.data_stores.blob.s3 import S3Client
from application.ml_model_operations.model_writer import ModelWriter
from application.column_transformation_operations.column_transformer_writer import ColumnTransformerWriter
from application.ml_model_trainers.saint.martyred import MartyredModelTrainer


class Container(object):

    def __init__(self) -> None:
        self.data_warehouse_connection_manager = ConnectionManager(getenv('SAINT_ANALYTICS_DB_CONNECTION_STRING'))
        self.data_warehouse_read_repository = ReadRepository(self.data_warehouse_connection_manager)
        self.ml_model_data_query_handler = MLModelQueryHandler(self.data_warehouse_read_repository)
        self.blob_client = S3Client(client('s3',
                                        #    endpoint_url=getenv('AWS_S3_ENDPOINT'),
                                           use_ssl=False,
                                           verify=False))
        self.model_writer = ModelWriter(self.blob_client)
        self.column_transformer_writer = ColumnTransformerWriter(self.blob_client)
        self.martyred_model_trainer = MartyredModelTrainer(self.ml_model_data_query_handler,
                                                           self.model_writer,
                                                           self.column_transformer_writer)
