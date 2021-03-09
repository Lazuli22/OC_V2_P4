from joueur import Joueur
from seriable import Serializable


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
        data_dict = {}
        data_dict['nom'] = self.nom
        data_dict['joueur1'] = self.match["joueur1"][0].serialize()
        data_dict['r1'] = self.match["joueur1"][1]
        data_dict['joueur2'] = self.match["joueur2"][0].serialize()
        data_dict['r2'] = self.match["joueur2"][1]
        return data_dict


def main():
    dolores = Joueur("Diaz", "Dolores", "1978-08-22", "Female", 100)
    tom = Joueur("Dupond", "Tom", "1980-11-20", "Male", 300)
    un_match = Match("match 1", dolores, 0, tom, 0)
    print(un_match.serialize())


if __name__ == "__main__":
    main()
