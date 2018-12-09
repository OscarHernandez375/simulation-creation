from domain.unit_operation import *
from domain.stream import Stream


class Simulation:

    def __init__(self, name):
        self.name = name
        self.streams: Set[Stream] = set()
        self.unit_operations: Set[UnitOperation] = set()
        self.energy_streams: Set[EnergyStream] = set()
        self.packages = set()

    def search_stream_by_name(self, stream_name: str):
        filtered = list(filter(lambda s: stream_name == s.name, self.streams))
        return filtered.pop() if filtered else None
