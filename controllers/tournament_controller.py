from ..models.element import Element_tournoi
from models.joueur import Joueur
from models.tournoi import Tournoi


class TournoiControlleur:

    def __init__(self, liste_data):
        self.__tournoi = Element_tournoi.creer_element(liste_data)
        self.__registre_joueurs = Joueur.liste_identifiants_joueurs(self.__tournoi.list_joueurs)


def main():
    liste_joueurs = Joueur.liste_identifiants_joueurs(Joueur.lecture_joueurs_json())
    tournoi_data = {'nom': 'Tournoi du Monde',
                    'lieu': 'Paris',
                    'date': '2021-03-13',
                    'list_joueurs': liste_joueurs,
                    'regle_temps': Tournoi.Regle_Temps.Blitz,
                    'description': 'Tournoi de renomée mondiale qui permet qui fait affonter les meilleurs joueurs mondiaux'
                    }
    un_tournoi = TournoiControlleur(**tournoi_data)
    print(un_tournoi.serialize())


if __name__ == "__main__":
    main()
