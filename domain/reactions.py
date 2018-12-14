from abc import ABC
from typing import Dict

from domain.component import Component


class Reaction(ABC):
    def __init__(self):
        self.__reactants: Dict[Component, float] = {}
        self.__products: Dict[Component, float] = {}

    @property
    def reactants(self):
        return self.__reactants

    @property
    def products(self):
        return self.__products


class StoichiometricReaction(Reaction):
    def __init__(self):
        super().__init__()
        self.__conversion: [Component, float] = []
        self.__limit_reactants: Component = None

    @property
    def conversion(self):
        return self.__conversion

    @property
    def limit_reactants(self):
        return self.__limit_reactants

    def conversion_setter(self, component: Component, conversion: float):
        component = component if self.reactants.__contains__(component) else None
        self.__conversion.append(component)
        self.__conversion.append(conversion)
        return self

    def calc_limit_reactant(self, inputs):
        minimum = min(inputs[x][0] / inputs[x][1] for x in inputs)
        self.__limit_reactants = list(
            map(lambda x: x, filter(lambda x: inputs[x][0] / inputs[x][1] == minimum, inputs)))
        return self


class RigorousReaction(Reaction):
    def __init__(self):
        super().__init__()
        self.__kinetics = ""
        self.__reaction_constant = 0
        self.__activation_energy = 0

    @property
    def kinetics(self):
        return self.__kinetics

    @property
    def reaction_constant(self):
        return self.__reaction_constant

    @property
    def activation_energy(self):
        return self.__activation_energy
