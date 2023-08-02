from boto3 import client
from config import settings
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Singleton
from data_access.data_stores.sql.connection_manager import ConnectionManager
from data_access.data_stores.sql.repositories.read import ReadRepository
from data_access.data_stores.sql.query_handlers.ml_model_data import MLModelQueryHandler
from data_access.data_stores.blob.s3 import S3Client
from application.ml_model_operations.model_writer import ModelWriter
from application.column_transformation_operations.column_transformer_writer import ColumnTransformerWriter
from application.ml_model_trainers.saint.martyred import MartyredModelTrainer
from core.utilities.startup import train_models


class Container(DeclarativeContainer):

    __config = Configuration()

    __config.from_dict(settings)

    environment = __config.environment()

    # data access
    __data_warehouse_connection_manager = Singleton(ConnectionManager,
                                                    connection_string=__config.sql.data_warehouse.connection_string())

    __data_warehouse_read_repository = Singleton(ReadRepository, connection_manager=__data_warehouse_connection_manager)

    __ml_model_data_query_handler = Singleton(MLModelQueryHandler, read_repository=__data_warehouse_read_repository)
    # data access

    # blob
    __blob_client = Singleton(S3Client,
                              s3_client=client('s3',
                                               region_name=__config.aws.region(),
                                               aws_access_key_id=__config.aws.access_key_id(),
                                               aws_secret_access_key=__config.aws.access_key_secret(),
                                               endpoint_url=__config.blob.s3.endpoint()))
    # blob

    # application

    # ml model ops
    __model_writer = Singleton(ModelWriter, blob_client=__blob_client)
    # ml model ops

    # column transformer ops
    __column_transformer_writer = Singleton(ColumnTransformerWriter, blob_client=__blob_client)
    # column transformer ops

    # model trainers
    __martyred_model_trainer = Singleton(MartyredModelTrainer,
                                         query_handler=__ml_model_data_query_handler,
                                         model_writer=__model_writer,
                                         column_transformer_writer=__column_transformer_writer)
    # model trainers

    # initialization
    train_models([
        __martyred_model_trainer()
    ])
    # initialization
