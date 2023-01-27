from data_access.data_stores.sql.queries.ml_model_data.saint import *
from core.enums.prediction_type import PredictionType

class MLModelDataQueryResolver(object):

    def __init__(self) -> None:
        pass

    @staticmethod
    def resolve_query(prediction_type: PredictionType) -> str:
        match prediction_type:
            case PredictionType.MARTYRED:
                return MARTYRED_QUERY
            case _:
                return None
