from os import getenv
from tensorflow.keras import Model
from ...core.constants.blob_directory_names import MODELS_DIRECTORY_NAME
from ...core.enums.prediction_type import PredictionType
from ...data_access.data_stores.blob.base import BaseBlobClient
from ..resolvers.blob_file_names.ml_model import MLModelFileNameResolver


class ModelWriter(object):

    def __init__(self,
                 blob_client: BaseBlobClient) -> None:
        self.__blob_client: BaseBlobClient = blob_client

    def save_model(self, prediction_type: PredictionType, model: Model) -> None:
        blob_name: str = MLModelFileNameResolver.resolve_file_name(prediction_type)

        models_directory_name: str = getenv('MODELS_DIRECTORY_NAME')

        self.__blob_client.post_blob(models_directory_name, blob_name, model.to_json())

        return
