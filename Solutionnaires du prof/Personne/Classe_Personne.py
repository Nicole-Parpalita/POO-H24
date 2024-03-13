
class Personne:
    """
    Classe Personne
    """
    # Attribut de classe
    ls_personnes = []
    dct_personnes = {}
    def __init__(self, p_nom: str = "", p_age: int = 0, p_nas : str =""):
        """
        Contructeur de la classe Personne
        :param p_nom: Nom de la personne
        :param p_age: Âge de la personne
        """
        self.nas = p_nas
        self._nom = p_nom
        self._age =p_age
        Personne.ls_personnes.append(self)
        Personne.dct_personnes[self.nas] = self

    # Propriétés à compléter ...
    def _get_age(self):
        """
        Accesseur (getter) de l'attribut _age
        :return: La valeur de l'attribut _age
        """
        return self._age
    def _set_age(self, v_age):
        """
        Accesseur (setter) de l'attribut _age
        :param v_age: nouvelle valeur de l'attribut -age
        :return:None
        """
        if isinstance(v_age, int) and 0 < v_age <= 130:
            self._age = v_age
    age = property(_get_age, _set_age)

    # Méthodes magiques
    def __add__(self, nb_annees: int):
        """
        Méthode magique qui permet de calculer la somme entre une instance Personne
        et un entier
        :param nb_annees: Le nombre d'années à ajouter à l'attribut âge.
        :return: None
        """
        self._age = self._age + nb_annees

    def __len__(self):
        """
        Méthode magique qui retourne l'âge de la personne
        :return: l'âge de la personne
        """
        return self._age

    def __str__(self):
        """
        Méthode magique qui permet de retourner les informations de la personne
        :return: une chaîne contenant le nom et l'âge de la personne
        """
        return f"{self._nom} a {self._age} ans."

    # Méthodes d'instances
    def feter_anniversaire(self):
        """
        Permet d'inscrémenter l'âge de la personne et d'afficher un message
        de félicitation.
        :return: None
        """
        self._age += 1
        print("Meilleurs voeux !!!")

    # Méthodes statiques
    @staticmethod
    def est_majeur(une_personne: "Personne"):
        """
        Vérifie si la personne est majeure ou mineure
        :param une_personne: Une instance de la classe Personne
        :return: True si la personne est majeure sinon elle retourne False
        """
        if une_personne._age >= 18:
            return True
        else:
            return False
    @staticmethod
    def afficher_liste(ls_personnes:list):
        """
        Affiche tout les éléments d'un liste
        :return: None
        """
        for elt in ls_personnes:
            print(elt)

    # Méthode de classe

    @classmethod
    def trouver_personnes_majeures_lst(cls):
        """
        Chercher dans la liste statique la liste des personnes majeures
        et la retourner
        :return: La liste des personnes majeures
        """
        ls_majeures = []
        for elt in cls.ls_personnes:
            if Personne.est_majeur(elt) is True:
                ls_majeures.append(elt)
        return ls_majeures

    @classmethod
    def trouver_personnes_majeures_dict(cls):
        """
        Chercher dans le dictionnaire statique la liste des personnes majeures
        et la retourner
        :return: La liste des personnes majeures
        """
        ls_majeures = []
        for cle in cls.dct_personnes.keys():
            if Personne.est_majeur(cls.dct_personnes[cle]) is True:
                ls_majeures.append(cls.dct_personnes[cle])
        return ls_majeures



