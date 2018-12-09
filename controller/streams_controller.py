from typing import Set

import jsonpickle
from flask import Flask

from domain.energy_stream import EnergyStream
from domain.simulation import Simulation

app = Flask(__name__)


@app.route('/simulation/', methods=["POST"])
@app.route('/simulation/<name>', methods=["POST"])
def create_simulation_environment(name="simulation_1"):
    simulation = Simulation(name)
    Environment().simulations.add(simulation)
    return jsonpickle.encode(simulation)


@app.route('/<simulation>/energy-stream/', methods=["POST"])
@app.route('/<simulation>/energy-stream/<name>', methods=["POST"])
def create_energy_stream(name="energy_stream_1", simulation=""):
    energy_stream = EnergyStream(name)
    simulation_search: list = list(filter(lambda s: simulation.__eq__(s.name), Environment.simulations))
    simulation_search[0].energy_streams.add(energy_stream)
    return jsonpickle.encode(energy_stream)


@app.route('/simulations', methods=["GET"])
def get_simulations():
    return jsonpickle.encode(Environment.simulations)


class Environment(object):
    simulations: Set[Simulation] = set()


if __name__ == '__main__':
    app.run()
