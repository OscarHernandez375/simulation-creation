from typing import Set

import jsonpickle

from domain.energy_stream import EnergyStream
from domain.simulation import Simulation
from domain.stream import Stream


def simulation_creation(name: str):
    simulation = Simulation(name)
    Environment().simulations.add(simulation)
    return jsonpickle.encode(simulation)


def energy_stream_creation(name, simulation):
    energy_stream = EnergyStream(name)
    simulation_search: list = list(filter(lambda s: simulation.__eq__(s.name), Environment.simulations))
    simulation_search[0].energy_streams.add(energy_stream)
    return jsonpickle.encode(energy_stream)


def stream_creation(name, simulation):
    stream = Stream(name)
    simulation_search: list = list(filter(lambda s: simulation.__eq__(s.name), Environment.simulations))
    simulation_search[0].streams.add(stream)
    return jsonpickle.encode(stream)


class Environment(object):
    simulations: Set[Simulation] = set()
