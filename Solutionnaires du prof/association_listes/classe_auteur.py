
class Auteur:
    """
    Classe qui permet de décrire un auteur
    """
    def __init__(self, p_cod_auteur: str = "", p_nom: str = "",
                 p_prenom: str = "", p_lst_livres: list = None):
        """
        Constructeur de la classe Auteur
        :param p_cod_auteur: Code de l'auteur
        :param p_nom: Nom de l'auteur
        :param p_prenom: Prénom de l'auteur
        :param p_lst_livres: Liste des livres écrits par un auteur
        """
        self.cod_auteur = p_cod_auteur
        self.nom = p_nom
        self.prenom = p_prenom
        if p_lst_livres is None:
            self.lst_livres = []
        else:
            self.lst_livres = p_lst_livres

    def retourner_infos(self):
        """
        Retourne les informations d'un auteur
        :return: Une chaîne qui contient l'information
        """
        return (f"Code : {self.cod_auteur}\n"
                f"Prénom: {self.prenom}\n"
                f"Nom: {self.nom}")

    def __str__(self):
        """
        Méthode magique qui retourne les informations d'un auteur
        :return: chaîne qui contient les informations d'un auteur
        """
        return (f"Code auteur  : {self.cod_auteur}\n"
                f"Prénom       : {self.prenom}\n"
                f"Nom          : {self.nom}")