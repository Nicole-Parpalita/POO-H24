from datetime import datetime
from classe_Cours import Cours

class Etudiant:
    """
    Classe Étudiant
    """
    ls_etudiants = []
    def __init__(self, p_num_etudiant: int = 0, p_nom: str = "", p_programme: str = "",
                 p_date_naissance: datetime = None, p_ls_cours: list = []):
        """
        Constructeur de la classe Etudiant
        :param p_num_etudiant: Le numéro étudiant de l'étudiant
        :param p_nom: Le nom de l'étudiant
        :param p_programme: Le programme de l'étudiant
        :param p_date_naissance: La date de naissance de l'étudiant
        """
        self._num_etudiant = p_num_etudiant
        self._nom = p_nom
        self._programme = p_programme
        self._date_naissance = p_date_naissance
        self._ls_cours = p_ls_cours
        Etudiant.ls_etudiants.append(self)

    def _get_num_etudiant(self):
        return self._num_etudiant

    def _set_num_etudiant(self, v_num_etudiant: int):
        if isinstance(v_num_etudiant, int) and len(str(v_num_etudiant)) == 7:
            self._num_etudiant = v_num_etudiant

    num_etudiant = property(_get_num_etudiant, _set_num_etudiant)

    def _get_nom(self):
        return self._nom

    def _set_nom(self, v_nom: str):
        if isinstance(v_nom, str) and len(v_nom) < 25:
            self._nom = v_nom

    nom = property(_get_nom, _set_nom)

    def _get_programme(self):
        return self._programme

    def _set_programme(self, v_programme: str):
        self._programme = v_programme

    programme = property(_get_programme, _set_programme)

    def _get_date_naissance(self):
        return self._date_naissance

    def _set_date_naissance(self, v_date_naissance):
        self._date_naissance = v_date_naissance

    def _get_ls_cours(self):
        return self._ls_cours

    def _set_ls_cours(self, v_ls_cours):
        self._ls_cours = v_ls_cours

    ls_cours = property(_get_ls_cours, _set_ls_cours)

    def afficher_liste_etudiants(cls):
        """
        Affiche les étudiants instanciés dans la classe
        """
        for etudiant in cls.ls_etudiants:
            print(etudiant)

    def associer_cours(self, cours):
        """
        Associer un cours à un étudiant
        """
        self.ls_cours.append(cours)

    def age(self):
        """
        Permet de calculer l'age de l'étudiant instancié
        """
        if self._date_naissance:
            ajd = datetime.date.today()
            return ajd.year - v_date_naissance.year() - ((ajd.month, ajd.day) <
                                                         (v_date_naissance.month, v_date_naissance.day))

    def afficher_ls_cours(self):
        """
        Permet d'afficher les cours de l'étudiant
        """
        print("Voici les cours de cet étudiant: ")
        for cours in self._ls_cours:
            print(cours)

    @classmethod
    def chercher_etudiant(cls, numero_etudiant):
        """
        Permet de chercher un étudiant dans la liste des étudiants par son numéro étudiant
        :param numero_etudiant: Le numéro étudiant de l'étudiant
        """
        for etudiant in cls.ls_etudiants:
            if etudiant._num_etudiant == numero_etudiant:
                return etudiant
        return None

    def __str__(self):
        """
        Méthode magique qui affiche toutes les informations de l'étudiant
        """
        return (f"""
*************************************

Numéro étudiant: {self._num_etudiant}
Nom: {self._nom}
Programme: {self._programme}
Age: {self.age()}

*************************************""")