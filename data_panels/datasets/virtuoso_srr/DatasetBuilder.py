import imp
import os
from pathlib import Path
import pandas as pd
from data_panels.datasets.interface.Dataset import Dataset
from srrpython.srr_python.pysrr import pysrrDataBase
from data_panels.datasets.virtuoso.SrrOutputsCsvFile import SrrOutputsCsvFile

from data_panels.datasets.interface.TestBench import TestBench

class PsfDatasetReader():
    "Reads in a PSF data using the pysrr library"

    ANALYSES = (
        ("tran-tran", "transient"),
    )

    def __init__(self, dataset_path: os.PathLike) -> None:
        self._path: Path = Path(dataset_path)
        self.database: pysrrDataBase = pysrrDataBase(self.path)
        

    @staticmethod
    def build(dataset_path: os.PathLike) -> Dataset:
        reader = PsfDatasetReader(dataset_path)
        return Dataset(
            table=reader.build_table(),
            test_bench=TestBench(),
            parameters=None,
        )

    def build_table(self) -> pd.DataFrame:
        results_table = self.read_results_table()
        signals_table = self.read_signals()

    def read_results_table(self):
        result =  pd.read_csv(self.test_bench_path / "maestro_output_results.csv")
        result = result.drop(columns=["Spec", "Weight","Pass/Fail"])
        return result.pivot_table(columns="Output")

    def read_signals(self):
        outputs = SrrOutputsCsvFile(self.test_bench_path / "maestro_outputs.csv").df
        for test in self.tests:
            self.read_analyses(test)

    def read_analyses(self, test: str) -> pd.DataFrame:
        database = pysrrDataBase(self.path / "psf" / test / "psf")
        dataset_names = database.dataSetNameList()
        for dataset_name in database.dataSetNameList():
            dataset = database.getDataSet(dataset_name)

    @property
    def tests(self):
        return [path.name for path in (self.path / "psf").iterdir()]

    @property
    def path(self):
        return self._path

    @property
    def test_bench_path(self):
        return self._path / "test_bench"