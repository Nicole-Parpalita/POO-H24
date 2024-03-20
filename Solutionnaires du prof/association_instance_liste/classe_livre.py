from classe_auteur import Auteur
class Livre:
    """
    Classe qui décrit un livre
    """
    def __init__(self, p_isbn: str = "", p_titre: str = "", p_auteur: Auteur = None):
        """
        Constructeur de la classe Livre
        :param p_isbn: ISBN du livre
        :param p_titre: Titre du livre
        :param p_lst_auteur : La liste des auteurs du livre
        """
        self.isbn = p_isbn
        self.titre = p_titre
        self.auteur = p_auteur

    def __str__(self):
        """
        Méthode magique qui retourne les informations du livre
        :return: Chaîne contenant les informations du livre
        """

        return(f"ISBN : {self.isbn}\n"
               f"Titre : {self.titre}")






