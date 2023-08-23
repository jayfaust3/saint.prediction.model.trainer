from typing import Union
from os import getenv
from ...queries.etl.fact_saint_martyred_loader import *
from ...queries.ml_model_data.saint import *
from ......core.enums.prediction_type import PredictionType


class MLModelDataQueryResolver(object):

    @staticmethod
    def resolve_query(prediction_type: PredictionType) -> Union[str, None]:
        match prediction_type:
            case PredictionType.MARTYRED:
                saint_martyred_fact_table_name: str = getenv('SAINT_ANALYTICS_DB_SAINT_MARTYRED_FACT_TABLE_NAME')
                saint_lake_table_name: str = getenv('SAINT_ANALYTICS_DB_SAINT_LAKE_TABLE_NAME')
                loader_query: str = FACT_SAINT_MARTYRED_LOADER_QUERY.format(saint_martyred_fact_table_name=saint_martyred_fact_table_name, saint_lake_table_name=saint_lake_table_name)
                formatted_martyred_query: str = MARTYRED_QUERY.format(saint_martyred_fact_table_name=saint_martyred_fact_table_name)
                return '{loader_query} {formatted_martyred_query}'.format(loader_query=loader_query, formatted_martyred_query=formatted_martyred_query)
            case _:
                return None
