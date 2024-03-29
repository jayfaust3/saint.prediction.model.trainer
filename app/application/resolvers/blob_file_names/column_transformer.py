from typing import Union
from ....core.enums.prediction_type import PredictionType
from ....core.constants.blob_file_names.column_transformer import *


class ColumnTransformerFileNameResolver(object):

    @staticmethod
    def resolve_file_name(prediction_type: PredictionType) -> Union[str, None]:
        match prediction_type:
            case PredictionType.MARTYRED:
                return MARTYRED_COLUMN_TRANSFORMER_FILE_NAME
            case _:
                return None
