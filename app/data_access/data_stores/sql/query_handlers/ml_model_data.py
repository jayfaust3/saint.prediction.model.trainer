from pandas import DataFrame
from .....core.enums.prediction_type import PredictionType
from ..repositories.read import ReadRepository
from ..resolvers.query.ml_model_data import MLModelDataQueryResolver


class MLModelQueryHandler(object):

    def __init__(self,
                 read_repository: ReadRepository) -> None:
        self.__read_repository: ReadRepository = read_repository

    def query_for_model_data(self, prediction_type: PredictionType) -> DataFrame:
        sql: str = MLModelDataQueryResolver.resolve_query(prediction_type)

        results: DataFrame = self.__read_repository.read(sql)

        return results
