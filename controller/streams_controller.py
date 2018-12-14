from typing import List

import jsonpickle
from flask import Flask

from domain.energy_stream import EnergyStream
from domain.reactors import StoichiometricReactor
from domain.simulation import Simulation, Stream
from services.simulation_service import Environment, simulation_creation, energy_stream_creation, stream_creation

app = Flask(__name__)

stream_count = 1
energy_stream_count = 1
simulation_count = 1
stoichiometric_reactor_count = 1


@app.route('/simulation/', methods=["POST"])
@app.route('/simulation/<name>', methods=["POST"])
def create_simulation_environment(name="simulation_1"):
    return simulation_creation(name)


@app.route('/<simulation>/energy-stream/', methods=["POST"])
@app.route('/<simulation>/energy-stream/<name>', methods=["POST"])
def create_energy_stream(name="energy_stream_1", simulation="simulation_1"):
    return energy_stream_creation(name,simulation)


@app.route('/<simulation>/stream/', methods=["POST"])
@app.route('/<simulation>/stream/<name>', methods=["POST"])
def create_stream(name="stream_1", simulation="simulation_1"):
    return stream_creation(name,simulation)


@app.route('/<simulation>/stoichiometric_reactor/', methods=["POST"])
@app.route('/<simulation>/stoichiometric_reactor/<name>', methods=["POST"])
def create_stoichiometric_reactor(name="reactor_1", simulation="simulation_1"):
    reactor = StoichiometricReactor(name)
    simulation_search: List[Simulation] = list(filter(lambda s: simulation.__eq__(s.name), Environment.simulations))
    simulation_search[0].unit_operations.add(reactor)
    return jsonpickle.encode(reactor)


@app.route('/simulations', methods=["GET"])
def get_simulations():
    return jsonpickle.encode(Environment.simulations)



if __name__ == '__main__':
    app.run()
