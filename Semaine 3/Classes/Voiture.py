class Voiture:
    """
    Classe Voiture
    """
    def __init__(self, p_marque: str, p_modele: str):
        """
        Constructeur de la classe Voiture
        :param p_marque: La marque de la voiture
        :param p_modele: Le modèle de la voiture
        """
        self.marque = p_marque
        self.modele = p_modele


    def afficher_informations(self):
        """
        Affiche les informations de la voiture
        :return: None
        """
        print("La marque de la voiture est", self.marque)
        print("Le modele de la voiture est", self.modele)