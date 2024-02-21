class Personne:
    """
    Classe Personne
    """
    # Attribut de classe
    ls_personnes = []
    def __init__(self, num_ass_soc: str = "", nom: str = "", age: int = 0):
        """
        Constructeur de la classe Personne
        :param nom: Le nom de la personne
        :param age: L'âge de la personne
        """
        self.num_ass_soc = num_ass_soc
        self.nom = nom
        self.age = age
        Personne.ls_personnes.append(self)

    def __str__(self):
        return f"Le nom de la personne est {self.nom} et son âge est de {self.age} ans."
    def __add__(self, annee):
        return f"{self.age + annee}"

    def __len__(self):
        return self.age

    def feter_anniversaire(self):
        nouvel_age = self.age + 1
        return f"Félicitations! Vous avez {nouvel_age} ans!"

    @staticmethod
    def est_majeur(age: int):
        """
        Prend une personne en paramètre et établi si il est majeur ou non
        :param age: L'âge de la personne
        :return: True si la personne est majeure (âge >= 18), sinon elle renvoie False
        """
        if age >= 18:
            return True
        else:
            return False

    @classmethod
    def trouver_personnes_majeures(cls):
        for element in cls.ls_personnes:
            if element.est_majeur == True:
                return element