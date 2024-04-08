class Cours:
    """
    Classe Cours
    """
    ls_cours = []
    def __init__(self, p_sigle: str = "", p_nom: str = "", p_nb_heures: int = 0):
        """
        Constructeur de la classe Cours
        :param p_sigle: Le sigle du cours
        :param p_nom: Le nom du cours
        :param p_nb_heures: Le nombre d'heures du cours
        """
        self._sigle = p_sigle
        self._nom = p_nom
        self._nb_heures = p_nb_heures
        Cours.ls_cours.append(self)

    def _get_sigle(self):
        return self._sigle

    def _set_sigle(self, v_sigle):
        if isinstance(v_sigle, str) and len(v_sigle) == 5:
            self._sigle = v_sigle

    sigle = property(_get_sigle, _set_sigle)

    def _get_nom(self):
        return self._nom

    def _set_nom(self, v_nom):
        if isinstance(v_nom, str) and len(v_nom) <= 50:
            self._nom = v_nom

    nom = property(_get_nom, _set_nom)

    def _get_nb_heures(self):
        return self._nb_heures

    def _set_nb_heures(self, v_nb_heures):
        if isinstance(v_nb_heures, int) and v_nb_heures <= 10:
            self._nb_heures = v_nb_heures

    nb_heures = property(_get_nb_heures, _set_nb_heures)

    def __str__(self):
        """
        Méthode magique qui affiche les informations du cours instancié
        """
        return (f"""*******************************
Sigle : {self._sigle}
Nom du cours: {self._nom}
Nombre d'heures : {self._nb_heures}
*******************************""")