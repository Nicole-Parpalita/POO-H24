from Auteur import Auteur

class Livre:
    """
    Classe qui décrit un livre
    """
    def __init__(self, p_isbn: str = "", p_titre: str = "", p_auteur: Auteur = None):
        """
        Constructeur de la classe Livre
        :param p_isbn: L'ISBN du livre
        :param p_titre: Le titre du livre
        :param p_auteur: L'auteur du livre
        """
        self.isbn = p_isbn
        self.titre = p_titre
        self.auteur = p_auteur