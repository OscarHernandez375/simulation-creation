class Component(object):
    def __init__(self, molecular_weight, name, formation_enthalpy, chemical_formula, density):
        self.__molecular_weight = molecular_weight
        self.__name = name
        self.__formation_enthalpy = formation_enthalpy
        self.__chemical_formula = chemical_formula
        self.__density = density

    @property
    def molecular_weight(self)->int:
        return self.__molecular_weight

    @property
    def name(self):
        return self.__name

    @property
    def formation_enthalpy(self):
        return self.__formation_enthalpy

    @property
    def chemical_formula(self):
        return self.__chemical_formula

    @property
    def density(self):
        return self.__density
