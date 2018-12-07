import numpy as np

from domain.component import Component


class Stream(object):

    def __init__(self, name):
        self.name = name
        self.__molar_composition = {}
        self.__temperature = 273.15
        self.__pressure = 1
        self.__mass_flow = 0
        self.__molar_flow = 0

    @property
    def molar_composition(self) -> {}:
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

    @mass_flow.setter
    def mass_flow(self, mass_flow):
        if mass_flow > 0:
            self.__mass_flow = mass_flow
        self.__molar_from_mass_flow()

    @property
    def molar_flow(self):
        return self.__molar_flow

    @molar_flow.setter
    def molar_flow(self, molar_flow):
        if molar_flow > 0:
            self.__molar_flow = molar_flow
        self.__mass_from_molar_flow()

    def add_update_component(self, component, composition=0):
        if 0 <= composition <= 1:
            self.__molar_composition[component] = composition

    def delete_component(self, component):
        del self.__molar_composition[component]

    def __mass_from_molar_flow(self):
        result = []
        for key, value in self.__molar_composition.items():
            result.append(key.molecular_weight * value)
        result = np.multiply(result, self.__molar_flow)
        self.__mass_flow = np.sum(result)

    def __molar_from_mass_flow(self):
        result = np.array([])
        for key, value in self.__molar_composition.items():
            np.append(result, (key.molecular_weight * value))
        result = np.multiply(result, self.__mass_flow)
        self.__molar_flow = np.sum(result)


class EnergyStream(object):
    def __init__(self, name):
        self.name = name
        self.__power = 0.0

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power
