from domain.unit_operation import *


class Simulation(object):

    def __init__(self, name):
        self.name = name
        self.streams: Set[Stream] = set()
        self.unit_operations: Set[UnitOperation] = set()
        self.energy_streams: Set[EnergyStream] = set()
        self.packages = set()
