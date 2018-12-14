from typing import List

from domain.component import Component
from domain.reactions import Reaction


class package:
    def __init__(self, name, reactions, components):
        self.__name: str = name
        self.__reactions: List[Reaction] = reactions
        self.__components: List[Component] = components