class Auteur:
    """
    Classe qui décrit un auteur
    """

    def __init__(self, p_code_auteur: str = "", p_nom: str = "", p_prenom: str = ""):
        """
        Constructeur de la classe Auteur
        """
        self.code_auteur = p_code_auteur
        self.nom = p_nom
        self.prenom = p_prenom
