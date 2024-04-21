from Animal import Animal
class Chat(Animal):
    """
    Classe oiseau, dérivée de la classe Animal
    """
    def __init__(self, p_poids : float = 0.0, p_couleur_poils : str = ""):
        """
        Constructeur de la classe Chat
        :param p_poids: Le poids du chat
        :param p_couleur_poils: La couleur de poils du chat
        """
        Animal.__init__(self, p_poids)
        self.couleur_poils = p_couleur_poils

    def __str__(self):
        """
        Fonction magique qui retourne les infos du chat
        """
        chaine = ("Le poids du chat est : " + str(self.poids) + " et la couleur de ses poils est : " +
                 str(self.couleur_poils))
        return chaine