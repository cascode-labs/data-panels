from typing import List
import numpy as np


class Waveform():
    def __init__(self, 
                 x: np.ndarray = np.ndarray(1),
                 y: np.ndarray = np.ndarray(1),
                 base_units: List[str] = ['', ''],
                 si_prefixes: List[str] = ['', '']
                ) -> None:
        self.x = x
        self.y = y
        self.base_units = base_units
        self.si_prefixes = si_prefixes