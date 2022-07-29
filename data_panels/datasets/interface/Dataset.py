from typing import Dict, Union
import pandas as pd
from data_panels.datasets.interface.TestBench import TestBench
from data_panels.datasets.interface.Waveform import Waveform


class Dataset():
    def __init__(self, 
                 table: pd.DataFrame,
                 parameters: pd.DataFrame, # A table describing each column (parameter) in the dataset table
                 test_bench: TestBench,
                ) -> None:
        self._table: pd.DataFrame = table
        self._parameters = parameters
        self._test_bench = test_bench

    @property
    def table(self) -> pd.DataFrame:
        """
        A table with each row as a different set of conditions and each column as a 
        condition parameter or a measurement.
        """
        return self._table

    @property
    def test_bench(self) -> TestBench:
        return self._test_bench
