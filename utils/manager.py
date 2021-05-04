import abc
from tinydb import TinyDB


class Manager(abc.ABC):

    def __init__(self, type_element, key):
        """ Expliquer la logique + annotations """
        self.registry = {}
        self.type_element = type_element
        self.id_maker_function = key
        self.db = TinyDB('db.json')

    def create(self, *args, **kwargs):
        item = self.type_element(*args, **kwargs)
        self.registry[self.id_maker_function(item)] = item
        return item

    def find_by_id(self, id_item):
        try:
            return self.registry[id_item]
        except ValueError:
            print(f"Le registre de {self.type_element}")
            print(f" ne contient pas l'id {id_item}")

    def find_all(self):
        return list(self.registry.values())
    
    def find_all_keys(self):
        return list(self.registry.keys())

    def find_by_criteria(self, criteria_function):
        """ Recherche des items par propriété / critères """
        return [
                item for item in self.registry.values() if criteria_function(item)
            ]

    @abc.abstractmethod
    def load_from_json(self):
        pass

    @abc.abstractmethod
    def load_from_dbase(self):
        pass

    @abc.abstractmethod
    def save_to_json(self):
        pass

    @abc.abstractclassmethod
    def save_to_dbase(self):
        pass
