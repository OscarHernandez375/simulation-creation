from domain.unit_operation import UnitOperation, Stream
from typing import Set
from domain.reactions import *


class StoichiometricReactor(UnitOperation):
    def __init__(self):
        super().__init__()
        self.reactions: Set[StoichiometricReaction] = set()

    def mathematical_system(self):
        reaction_string = set(map(lambda s: s,self.input_streams))
        print(reaction_string)


class RigorousReactor(UnitOperation):
    def __init__(self):
        super().__init__()
        self.reactions: Set[RigorousReaction] = set()
        self.ua = 0.0

# s = StoichiometricReactor()
# c = Component(1,"H2",1,"H2",1)
# s.input_streams.add(Stream("s1").add_update_component(c))
# s.reactions.add(Reaction().reactants.__setitem__(c,1))
#
# s.mathematical_system()