class Animal:
    """
    Classe Animal
    """
    def __init__(self, p_poids : float = 0.0):
        """
        Constructeur de la classe Animal
        :param p_poids: Le poids de l'animal
        """
        self.poids = p_poids

    def __str__(self):
        """
        Retourne l'information de l'animal
        """
        chaine = "Le poids de l'animal est : " + str(self.poids) + "."
        return chaine
