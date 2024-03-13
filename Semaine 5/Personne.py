class Personne:
    """
    Classe Personne
    """
    # Attribut de classe
    ls_personnes = []
    dict_personnes = {}
    def __init__(self, num_ass_soc: str = "", nom: str = "", age: int = 0):
        """
        Constructeur de la classe Personne
        :param nom: Le nom de la personne
        :param age: L'âge de la personne
        """
        self.num_ass_soc = num_ass_soc
        self.nom = nom
        self._age = age
        Personne.ls_personnes.append(self)
        Personne.dict_personnes[self.num_ass_soc] = self

    def _get_age(self):
        return self._age

    def _set_age(self, v_age):
        if isinstance(v_age, int) and v_age > 0:
            self._age = v_age

    age = property(_get_age, _set_age)

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
        for instance in cls.ls_personnes:
            if instance.age >= 18:
                print(instance.nom)

    @classmethod
    def trouver_personnes_majeures2(cls):
        for num_ass_soc, personne in cls.dict_personnes.items():
            if personne.age >= 18:
                print(personne.nom)