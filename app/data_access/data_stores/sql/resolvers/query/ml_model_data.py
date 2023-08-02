from os import getenv
from data_access.data_stores.sql.queries.ml_model_data.saint import *
from core.enums.prediction_type import PredictionType


class MLModelDataQueryResolver(object):

    @staticmethod
    def resolve_query(prediction_type: PredictionType) -> str:
        match prediction_type:
            case PredictionType.MARTYRED:
                return MARTYRED_QUERY.format(saint_martyred_fact_table_name=getenv('SAINT_ANALYTICS_DB_SAINT_MARTYRED_FACT_TABLE_NAME'))
            case _:
                return None
