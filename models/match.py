from joueur import Joueur
from seriable import Serializable
from operator import attrgetter


class Match(Serializable):
    """ Classe représentant un match caractérisé par
        - une paire de joueurs
        - un champ résultat pour chaque joueur
    """

    def __init__(self, nom, joueur1, r1, joueur2, r2):
        """Contruscteur de la classe Match"""
        self.nom = nom
        self.match = {}
        self.match['joueur1'] = [joueur1, r1]
        self.match['joueur2'] = [joueur2, r2]

    def __repr__(self) -> str:
        """Fonction permettant d'afficher un match"""
        return (
            f"<match entre {self.match['joueur1'][0]} et"
            f"{self.match['joueur2'][0]},"
            f"score de joueur 1 ={self.match['joueur1'][1]},"
            f"score de joueur 2 = {self.match['joueur2'][1]}>"
            )

    def serialize(self) -> dict[str, str]:
        """ Fonction permettant de sérialiser  un match en retour, nous obtenons
            un dictionnaire des valeurs du Match"
        """
        return {
            'nom': self.nom,
            'joueur1': self.match["joueur1"][0].serialize(),
            'r1': self.match["joueur1"][1],
            'joueur2': self.match["joueur2"][0].serialize(),
            'r2': self.match["joueur2"][1]
        }

    def generer_matchs_premier_tour(list_joueur):
        """ fonction permettant de générer les matchs du 1er Tour,
            retournant une liste de matchs
        """
        list_triee = sorted(
                        list_joueur,
                        key=attrgetter("classement"),
                        reverse=True
                        )
        return [
            Match("Match1", list_triee[0], 0, list_triee[4], 0),
            Match("Match2", list_triee[1], 0, list_triee[5], 0),
            Match("Match3", list_triee[2], 0, list_triee[6], 0),
            Match("Match4", list_triee[3], 0, list_triee[7], 0)
        ]


def main():
    #dolores = Joueur("Diaz", "Dolores", "1978-08-22", "Female", 100)
    #tom = Joueur("Dupond", "Tom", "1980-11-20", "Male", 300)
    #un_match_data = Match("match 1", dolores, 0, tom, 0)
    #un_match = un_match_data.serialize()
    print(Match.generer_matchs_premier_tour(Joueur.lecture_joueurs_json()))


if __name__ == "__main__":
    main()
