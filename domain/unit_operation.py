from abc import ABC
from typing import Set

from domain.energy_stream import EnergyStream
from domain.stream import Stream


class UnitOperation(ABC):
    def __init__(self, name):
        self.name = name
        self.input_streams: [Stream] = []
        self.output_streams: [Stream] = []
        self.input_energy_streams: Set[EnergyStream] = set()
        self.output_energy_streams: Set[EnergyStream] = set()
        self.temperature = 273.15
        self.pressure = 1

