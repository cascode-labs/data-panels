import pandas as pd
from typing import Union, Optional


class SrrOutputsCsvFile:
    """class to [arse] the outputs csv file exported from Maestro"""

    def __init__(self, path: str):
        self._path: str = path
        self._df: Optional[pd.DataFrame] = None

    def _read_file(self) -> Union[pd.DataFrame, None]:
        if self._path is None:
            return None

        # noinspection PyBroadException
        try:
            df = pd.read_csv(
                self._path,
                keep_default_na=False,
                converters={
                    "Name": lambda x: str(x),
                    "Plot": lambda x: x != "",
                    "Save": lambda x: x != "",
                })
            return df
        except:
            return None

    def _validate(self):
        if self._df is None:
            self._logger.warning(f"Could not read outputs csv at {self._path}")
            return

        expected_columns = ('Test', 'Name', 'Type', 'Output', 'EvalType',
                            'Plot', 'Save', 'Spec')
        missing_columns = set(expected_columns) - set(self._df.columns)
        if len(missing_columns) > 0:
            self._logger.warning(
                f"Maestro Outputs CSV file is missing required columns!\n"
                f"csv file path: {self._path}\n"
                f"Missing column names: {', '.join(missing_columns)}")
        elif len(self._df) < 1:
            self._logger.warning(f"Empty outputs CSV file: {self._path}")

    @property
    def df(self) -> pd.DataFrame:
        if self._df is None:
            self._df = self._read_file()
            self._validate()
        return self._df
