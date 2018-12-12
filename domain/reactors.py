from typing import Set

from domain.reactions import *
from domain.stream import Stream
from domain.unit_operation import UnitOperation


class StoichiometricReactor(UnitOperation):
    def __init__(self):
        super().__init__()
        self.reactions: Set[StoichiometricReaction] = set()

    def single_stream_calculator(self):
        single_stream = [y for x in self.input_streams for y in [x.molar_composition]]

        print(single_stream)

    def calc_output_stream(self):
        result = {}
        for comp in [y for x in self.reactions for y in x.reactants.items()]:
            result.__setitem__(comp, 0)
        for comp in [y for x in self.reactions for y in x.products.items()]:
            result.__setitem__(comp, 0)
        for comp in [y for x in self.input_streams for y in x.molar_composition.items()]:
            result.__setitem__(comp, self.input_streams)

        for r in self.reactions:
            for comp in r.reactants:
                pass
            for comp in r.products:
                pass


class RigorousReactor(UnitOperation):
    def __init__(self):
        super().__init__()
        self.reactions: Set[RigorousReaction] = set()
        self.max_volume = 0.0
        self.actual_volume = 0.0
        self.ua = 0.0


s = StoichiometricReactor()
c1 = Component(1.0, "H2", 1.0, "H2", 1.0)
c2 = Component(2.0, "2H2", 1.0, "2H2", 1.0)
c3 = Component(1.0, "2H", 1.0, "2H", 1.0)
stream1 = Stream("s1")
stream2 = Stream("s2")
stream3 = Stream("s3")
r = StoichiometricReaction()
r.reactants.__setitem__(c1, 1.0)
r.reactants.__setitem__(c3, 1.0)
r.products.__setitem__(c2, 1.0)
r.conversion_setter(c1, 0.85)
s.input_streams.add(stream1)
s.input_streams.add(stream3)
s.output_streams.add(stream2)
stream1.add_update_component(c1, 100.0).add_update_component(c3, 100.0)
stream3.add_update_component(c1, 50.0).add_update_component(c3, 25.0)
s.reactions.add(r)

s.single_stream_calculator()
s.calc_output_stream()
