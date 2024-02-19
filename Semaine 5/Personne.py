class Personne:
    """
    Classe Personne
    """
    # Attribut de classe
    ls_personnes = []
    def __init__(self, nom: str = "", age: int = 0):
        """
        Constructeur de la classe Personne
        :param nom: Le nom de la personne
        :param age: L'âge de la personne
        """
        self.nom = nom
        self.age = age
        Personne.ls_personnes.append(self)

    def __add__(self, age):
        return self.age + age

    def __len__(self):
        return self.age


    def feter_anniversaire(self):