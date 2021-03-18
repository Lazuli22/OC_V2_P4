from typing import Callable, Any


class Factory:

    def __init__(self, craft_type, id_smith_func: Callable[[Any], str] = None):
        self.crafted = {}
        self.craft_type = craft_type
        self.id_smith_func = id_smith_func if id_smith_func else lambda x: id(x)

    def create(self, **params):
        obj = self.craft_type(**params)
        identifier = self.id_smith_func(obj)
        if identifier not in self.crafted:
            self.crafted[identifier] = obj
            return obj

    def find(self, identifier: str) -> Any:
        if identifier in self.crafted:
            return self.crafted[identifier]
        raise ValueError(identifier)
