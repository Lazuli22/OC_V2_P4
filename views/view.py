import abc
from utils.singleton import Singleton


class View(Singleton, metaclass=abc.ABCMeta):
    """ Abstract class to defines views of Chess Tournament"""
    def __init__(self):
        pass

    @abc.abstractclassmethod
    def show(self):
        pass

    def show_load_create(self, type_element):
        """ function that permits a create or load a element"""
        id_element = ""
        print(f"Voulez-vous créer (C) ou reprendre (R) un {type_element} ?")
        choix = input()
        if choix == "R":
            print(f"Veuillez fournir l'idenfiant du {type_element} à reprendre")
            id_element = input()
        return choix, id_element

    def quit(self):
        """ function that quits the program """
        print("Sortie du programme ! A bientôt")
