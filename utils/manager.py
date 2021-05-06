import abc
from tinydb import TinyDB


class Manager(abc.ABC):
    """
    Class that permits create a registry with generic type elements
    several functions are proposed to manipulate elements
    """

    def __init__(self, type_element, key):
        self.registry = {}
        self.type_element = type_element
        self.id_maker_function = key
        self.db = TinyDB('db.json')

    def create(self, *args, **kwargs):
        """
        function that creates and adds a element of specific type
        in a registry
        """
        item = self.type_element(*args, **kwargs)
        self.registry[self.id_maker_function(item)] = item
        return item

    def find_by_id(self, id_item):
        """
        function that finds an element from its key
        """
        try:
            return self.registry[id_item]
        except ValueError:
            print(f"Le registre de {self.type_element}")
            print(f"ne contient pas l'id {id_item}")

    def find_all(self):
        """
        function that gives all elements of a registry
        """
        return list(self.registry.values())

    def find_by_criteria(self, criteria_function):
        """ Recherche des items par propriété / critères """
        return [
                item for item in self.registry.values()
                if criteria_function(item)
            ]

    @abc.abstractmethod
    def load_from_dbase(self):
        pass

    @abc.abstractclassmethod
    def save_to_dbase(self):
        pass
