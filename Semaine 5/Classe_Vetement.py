class Vetement:
    """
    Classe Vetement
    """
    # Attribut de classe
    tissu = "Cotton"
    nb_vetements = 0
    ls_vetements = []
    def __init__(self, p_type: str = "", p_prix: float = 0.0,
                 p_long: float = 0.0, p_larg: float = 0.0):
        # Attributs d'instance
        self._type = p_type
        self.prix = p_prix
        self.long = p_long
        self.larg = p_larg
        Vetement.nb_vetements += 1
        Vetement.ls_vetements.append(self)

    # Propriétés
    def _get_type(self):
        return self._type

    def _set_type(self, v_type):
        if isinstance(v_type, str) and len(v_type) < 15:
            self._type = v_type

    type = property(_get_type, _set_type)

    # Les méthodes magiques
    def __add__(self, vet: "Vetement"):
        """
        Méthode magique qui permet d'additionner deux vêtements
        :param vet: Instance de la classe Vetement
        :return: Somme des prix des deux vêtements
        """
        return self.prix + vet.prix

    def __len__(self):
        """
        Méthode magique qui retourne la longueur d'un vêtement
        (sa longueur + sa largeur)
        :return: La somme de la longueur et la largeur du vêtement
        """
        return int(self.long + self.larg)

    # Méthodes de classe
    @classmethod
    def verifier_nb_instances(cls, nb_v: int):

        """
        Retourne True s'il y a plus d'instances que nb_v
        sinon elle retourne False
        :param nb_v: Le nombre d'instances
        :return: True si le nombre d'instances répond au critère
        False si non
        """
        if cls.nb_vetements >= nb_v:
            return True
        else:
            return False

    @classmethod
    def afficher_vetements(cls):
        for element in cls.ls_vetements:
            print(element)

    def __str__(self):
        """
        Permet d'afficher les infos d'un vêtement
        :return: Une chaîne de carcatères contenant les infos
        """
        return (f"\nType: {self._type}\n"
                f"Prix: {self.prix}\n")

    @staticmethod
    def somme(mesure1: float, mesure2: float):
        """
        Additionne deux mesures du vêtement et retourne leur somme
        :param mesure1: Première mesure prise du vêtement
        :param mesure 2: Deuxième mesure prise du vêtement
        :return: La somme de mesure1 and mesure2
        """
        return mesure1 + mesure2
