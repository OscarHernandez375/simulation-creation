from typing import Set

from domain.component import Component
from domain.reactions import *
from domain.stream import Stream
from domain.unit_operation import UnitOperation


class StoichiometricReactor(UnitOperation):
    def __init__(self):
        super().__init__()
        self.reactions: Set[StoichiometricReaction] = set()

    def reaction_math_system(self, reaction):
        input_stream_components = [y for x in self.input_streams for y in x.molar_composition]
        output_stream_components = [y for x in self.output_streams for y in x.molar_composition]
        input_component_names = [comp.name for comp in
               filter(lambda comp: comp in input_stream_components, reaction.reactants)]
        print(input_component_names)


class RigorousReactor(UnitOperation):
    def __init__(self):
        super().__init__()
        self.reactions: Set[RigorousReaction] = set()
        self.ua = 0.0


s = StoichiometricReactor()
c1 = Component(1.0, "H2", 1.0, "H2", 1.0)
c2 = Component(2.0, "2H2", 1.0, "2H2", 1.0)
stream1 = Stream("s1")
stream2 = Stream("s2")

reaction = StoichiometricReaction()
reaction.reactants.__setitem__(c1, 1.0)
reaction.products.__setitem__(c2, 1.0)
reaction.conversion = 0.85
s.input_streams.add(stream1)
s.output_streams.add(stream2)
stream1.add_update_component(c1, 1.0)
stream2.add_update_component(c2, 1.0)
stream2.add_update_component(c1, 1.0)
s.reactions.add(reaction)

s.reaction_math_system(reaction)
