from Auteur import Auteur

class Livre:
    """
    Classe qui décrit un livre
    """

    def __init__(self, p_isbn: str = "", p_titre: str = "", p_ls_auteurs : list[Auteur] = []):
        """
        Constructeur de la classe Livre
        :param p_isbn: L'ISBN du livre
        :param p_titre: Le titre du livre
        :param p_auteur: L'auteur du livre
        """
        self.isbn = p_isbn
        self.titre = p_titre
        self.ls_auteurs = p_ls_auteurs

    def __str__(self):
        """
        Retourne le titre du livre
        """
        return f"{self.titre}"

    def afficher_auteurs(self):
        """
        Affiche les auteurs du livre
        """
        for auteur in self.ls_auteurs:
            print(auteur.nom, auteur.prenom)