from typing import Dict

import numpy as np

from domain.component import Component


class Stream(object):

    def __init__(self, name):
        self.name = name
        self.__molar_composition: Dict[Component, float] = {}
        self.__temperature = 273.15
        self.__pressure = 1.0
        self.__mass_flow = 0.0
        self.__molar_flow = 0.0
        self.__avg_density = 0.0

    @property
    def molar_composition(self) -> {Component, float}:
        return self.__molar_composition

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        if temperature > 0:
            self.__temperature = temperature

    @property
    def pressure(self):
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure):
        self.__pressure = pressure

    @property
    def mass_flow(self):
        return self.__mass_flow

    @property
    def molar_flow(self):
        return self.__molar_flow

    @property
    def avg_density(self):
        return self.__avg_density

    def add_update_component(self, component, molar_flow=0.0):
        if 0 <= molar_flow:
            self.__molar_composition[component] = molar_flow
            self.__molar_total_from_composition()
            self.__mass_total_from_composition()
            self.__avg_density_from_composition()
            return self

    def delete_component(self, component):
        del self.__molar_composition[component]

    def __mass_total_from_composition(self):
        result = []
        for key, value in self.__molar_composition.items():
            result.append(key.molecular_weight * value)

        self.__mass_flow = np.sum(result)

    def __molar_total_from_composition(self):
        result = []
        for key, value in self.__molar_composition.items():
            result.append(value)
        self.__molar_flow = np.sum(result)

    def __avg_density_from_composition(self):
        result = []
        for key, value in self.__molar_composition.items():
            result.append(key.density * value * key.molecular_weight / self.__mass_flow)
        self.__avg_density = np.sum(result)
