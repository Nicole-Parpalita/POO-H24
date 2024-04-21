from Animal import Animal
class Oiseau(Animal):
    """
    Classe Oiseau, dérivée de la classe Animal
    """
    def __init__(self, p_poids: float = 0.0, p_longueur_bec: float = 0.0):
        """
        Constructeur de la classe Oiseau
        :param p_poids: Le poids de l'oiseau
        :param p_longueur_bec: La longueur du bec de l'oiseau
        """
        Animal.__init__(self, p_poids)
        self.longueur_bec = p_longueur_bec

    def __str__(self):
        """
        Fonction magique qui retourne les infos de l'oiseau
        """
        chaine = ("Le poids de l'oiseau est : " + str(self.poids) + " et la longueur de son bec est : " +
                  str(self.longueur_bec))
        return chaine