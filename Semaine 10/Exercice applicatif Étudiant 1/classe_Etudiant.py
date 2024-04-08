class Etudiant:
    """
    Classe Étudiant
    """
    ls_etudiants = []
    def __init__(self, p_num_etudiant: str = "", p_nom: str = "", p_prenom: str = "", p_programme: str = ""):
        """
        Constructeur de la classe Etudiant
        :param num_etudiant: Le numéro étudiant de l'étudiant
        :param nom: Le nom de l'étudiant
        :param prenom: Le prénom de l'étudiant
        :param programme: Le programme de l'étudiant
        """
        self._num_etudiant = p_num_etudiant
        self._nom = p_nom
        self._prenom = p_prenom
        self._programme = p_programme
        Etudiant.ls_etudiants.append(self)

    def _get_num_etudiant(self):
        return self._num_etudiant

    def _set_num_etudiant(self, v_num_etudiant: str):
        if isinstance(v_num_etudiant, str) and len(v_num_etudiant) == 7:
            self._num_etudiant = v_num_etudiant

    num_etudiant = property(_get_num_etudiant, _set_num_etudiant)

    def _get_nom(self):
        return self._nom

    def _set_nom(self, v_nom: str):
        if isinstance(v_nom, str) and len(v_nom) < 25:
            self._nom = v_nom

    nom = property(_get_nom, _set_nom)

    def _get_prenom(self):
        return self._prenom

    def _set_prenom(self, v_prenom: str):
        if isinstance(v_prenom, str) and len(v_prenom) < 25:
            self._prenom = v_prenom

    prenom = property(_get_prenom, _set_prenom)

    def _get_programme(self):
        return self._programme

    def _set_programme(self, v_programme: str):
        if isinstance(v_programme, str):
            self._programme = v_programme

    def __str__(self):
        """
        Méthode magique qui affiche toutes les informations de l'étudiant
        """
        return (f"""Numéro étudiant: {self._num_etudiant}
Nom: {self._nom}
Prenom: {self._prenom}
Programme: {self._programme}""")