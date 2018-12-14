from collections import Counter
from typing import Set

from domain.reactions import *
from domain.stream import Stream
from domain.unit_operation import UnitOperation


class StoichiometricReactor(UnitOperation):
    def __init__(self, name):
        super().__init__(name)
        self.reactions: Set[StoichiometricReaction] = set()

    def __single_stream_calculator(self) -> Dict:
        counter = Counter()
        stream_dictionaries = [x.molar_composition for x in self.input_streams]
        for dictionary in stream_dictionaries:
            counter.update(Counter(dictionary))
        single_stream = dict(counter)
        return single_stream

    def calc_output_stream(self):
        single_input: Dict = self.__single_stream_calculator()
        result_input = {}
        for comp in [y for x in self.reactions for y, z in x.reactants.items()]:
            result_input.__setitem__(comp, 0)
        for comp in [y for x in self.reactions for y, z in x.products.items()]:
            result_input.__setitem__(comp, 0)
        for comp, flow in single_input.items():
            result_input.__setitem__(comp, flow)
        for r in self.reactions:
            for comp, coef in r.reactants.items():
                self.output_streams[0].add_update_component(comp, result_input[comp] - coef / r.reactants[r.conversion[0]] * r.conversion[1] * result_input[
                    r.conversion[0]])
            for comp, coef in r.products.items():
                self.output_streams[0].add_update_component(comp, result_input[comp] + coef / r.reactants[r.conversion[0]] * r.conversion[1] * result_input[
                    r.conversion[0]])
        print(self.output_streams[0].molar_composition)


class RigorousReactor(UnitOperation):
    def __init__(self, name):
        super().__init__(name)
        self.reactions: Set[RigorousReaction] = set()
        self.max_volume = 0.0
        self.actual_volume = 0.0
        self.ua = 0.0


s = StoichiometricReactor("reac")
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
r2 = StoichiometricReaction()
r2.reactants.__setitem__(c1, 2.0)
r2.products.__setitem__(c2, 1.0)
r.conversion_setter(c3, 0.85)
r2.conversion_setter(c1, 1)
s.input_streams.append(stream1)
s.input_streams.append(stream3)
s.output_streams.append(stream2)
stream1.add_update_component(c1, 100.0).add_update_component(c3, 100.0)
stream3.add_update_component(c1, 50.0).add_update_component(c3, 25.0)
s.reactions.add(r)

s.calc_output_stream()
