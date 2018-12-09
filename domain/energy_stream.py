class EnergyStream:
    def __init__(self, name):
        self.name = name
        self.__power = 0.0

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power
