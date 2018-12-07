from abc import ABC
from typing import Set
from domain.streams import *


class UnitOperation(ABC):
    def __init__(self):
        self.input_streams: Set[Stream] = set()
        self.output_streams: Set[Stream] = set()
        self.input_energy_streams: Set[EnergyStream] = set()
        self.output_energy_streams: Set[EnergyStream] = set()
        self.temperature = 273.15
        self.pressure = 1
        self.max_volume = 0
        self.actual_volume = 0

    def mathematical_system(self):
        pass
