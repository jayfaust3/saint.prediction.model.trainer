from typing import List
from core.data_models.data_column import DataColumnModel
from core.enums.column_data_type import ColumnDataType

MARTYRED_TRANSFORMABLE_COLUMNS: List[DataColumnModel] = [
    DataColumnModel(column_name = 'year_of_death', data_type = ColumnDataType.INT),
    DataColumnModel(column_name = 'age_at_death', data_type = ColumnDataType.INT),
    DataColumnModel(column_name = 'region', data_type = ColumnDataType.STRING),
    DataColumnModel(column_name = 'target', data_type = ColumnDataType.BOOLEAN)
]
