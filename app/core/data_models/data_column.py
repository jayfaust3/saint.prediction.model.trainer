from core.enums.column_data_type import ColumnDataType


class DataColumnModel(object):

    def __init__(self,
                 column_name: str,
                 data_type: ColumnDataType) -> None:
        self.column_name: str = column_name
        self.data_type: ColumnDataType = data_type
