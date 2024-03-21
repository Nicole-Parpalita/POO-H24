from Equipe import Equipe
class JoueurSoccer:
    """
    Classe JoueurSoccer
    """
    # Attributs de classe
    lst_joueur_soccer = []

    def __init__(self, p_numero_joueur: int = -1, p_prenom: str = ""):
        """
        Constructeur de la classe JoueurSoccer
        :param p_numero_joueur: Le numéro du joueur instancié
        :param p_prenom: Le prénom du joueur instancié
        """
        self.numero_joueur = p_numero_joueur
        self.prenom = p_prenom
        JoueurSoccer.lst_joueur_soccer.append(self)

    # Méthodes
    @classmethod
    def trouver_liste_joueur(cls, p_equipe: Equipe):
        """
        Retourner la liste des joueurs qui jouent dans une équipe
        :param p_equipe: L'équipe dans laquelle les joueurs jouent
        """
        return p_equipe.ls_joueurs


    @staticmethod
    def calculer_prime_salaire(nb_buts: int, salaire: float) -> float:
        """
        Calculer la prime du joueur en fonction du nombre de buts
        :param nb_buts: Le nombre de buts marqués par ce joueur
        :param salaire: Le salaire du joueur
        :return: La prime du joueur
        """
        return nb_buts * (salaire * 0.1) + salaire

    def __str__(self):
        """
        Méthode magique
        :return: Une chaîne contenant le numéro du joueur et son prénom
        """
        return f"Le numéro de ce joueur est: {self.numero_joueur} et son prénom est: {self.prenom}."