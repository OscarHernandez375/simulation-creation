from abc import ABC
from typing import Set

from domain.energy_stream import EnergyStream
from domain.stream import Stream


class UnitOperation(ABC):
    def __init__(self):
        self.input_streams: Set[Stream] = set()
        self.output_streams: Set[Stream] = set()
        self.input_energy_streams: Set[EnergyStream] = set()
        self.output_energy_streams: Set[EnergyStream] = set()
        self.temperature = 273.15
        self.pressure = 1

