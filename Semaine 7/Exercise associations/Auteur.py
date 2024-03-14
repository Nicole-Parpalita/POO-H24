
class Auteur:
    """
    Classe qui décrit un auteur
    """
    def __init__(self, p_code_auteur: str = "", p_nom: str = "",
                 p_prenom: str = "", p_ls_livres : list = []):
        """
        Constructeur de la classe Auteur
        """
        self.code_auteur = p_code_auteur
        self.nom = p_nom
        self.prenom = p_prenom
        self.ls_livres = p_ls_livres

    def retourner_infos_auteur(self):
        """
        Retourne les informations de l'auteur
        :return: Les informations de l'auteur
        """
        return f"""Code: {self.code_auteur}
Prénom: {self.prenom}
Nom: {self.nom}"""

    # Peut aussi faire ça et mettre print(livre1.auteur)
    def __str__(self):
        """
        Retourne les informations de l'auteur
        :return: Les informations de l'auteur
        """
        return f"""Code: {self.code_auteur}
Prénom: {self.prenom}
Nom: {self.nom}"""

    def afficher_livres(self):
        """
        Afficher tous les livres écrits par l'auteur
        """
        print("Les livres écrits par cet auteur sont :")
        for livre in self.ls_livres:
            print(livre.titre)