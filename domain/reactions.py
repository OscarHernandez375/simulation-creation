from abc import ABC
from domain.component import Component
from typing import Dict


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
        self.__conversion = 0

    @property
    def conversion(self):
        return self.__conversion



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
