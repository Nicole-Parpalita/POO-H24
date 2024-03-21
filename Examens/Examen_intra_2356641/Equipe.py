class Equipe:
    """
    Classe Equipe
    """
    # Attributs de classe
    nb_equipes = 0

    def __init__(self, p_code_equipe: str = "", p_nom_equipe: str = "", p_ls_joueurs: list = []):
        """
        Constructeur de la classe Equipe
        """
        self.code_equipe = p_code_equipe
        self.nom_equipe = p_nom_equipe
        self.ls_joueurs = p_ls_joueurs
        Equipe.nb_equipes += 1

    # Méthodes
    @classmethod
    def niveau_ligue_soccer(cls):
        """
        Permet de retourner le niveau (1, 2 ou 3) de la ligue en fonction du nombre d’équipes qu’elle contient
        """
        niveau_ligue = 0
        if cls.nb_equipes <= 10:
            niveau_ligue = 1
        elif cls.nb_equipes <= 20:
            niveau_ligue = 2
        elif cls.nb_equipes > 20:
            niveau_ligue = 3
        return niveau_ligue

    def afficher_joueurs(self):
        """
        Afficher les informations des joueurs qui jouent dans cette équipe
        """
        print(f"Voici les joueurs de l'équipe {self.nom_equipe}:")
        for joueur in self.ls_joueurs:
            print(f"""Numéro: {joueur.numero_joueur} et Prenom: {joueur.prenom}""")

    def __str__(self):
        """
        Méthode magique
        :return: Une chaîne contenant le code de l'équipe et le nom de l'équipe
        """
        return f"Le code de cette équipe est: {self.code_equipe} et son nom est: {self.nom_equipe}."

