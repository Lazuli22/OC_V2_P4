from date import datetime


class Tournee:
    """
    Classe qui définit un Tour ou un round composé de
        - un nom
        - une liste de matchs
        - une date de début
        - une heure de début
        - une date de fin
        - une heure de fin
    """

    def __init__(self, nom, list_matchs):
        """ Contructeur pour instancier un tour """
        self.nom = nom
        self.liste_matchs = list_matchs
        self.date_debut = date.datetime.now()
        self.heure_debut = 0
        self.date_fin = None
        self.heure_fin = None


        


        
