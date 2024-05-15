class Local:
    """
    Classe Local
    """
    ls_locaux = []
    def __init__(self, p_type_local: str = "", p_num_local: str = "", p_lieu_local: str = "",
                 p_dimension_local: float = 0.0, p_nb_places: int = 0):
        """
        Constructeur de la classe Local
        """
        self.type_local = p_type_local
        self._num_local = p_num_local
        self.lieu_local = p_lieu_local
        self._dimension_local = p_dimension_local
        self._nb_places = p_nb_places
        Local.ls_locaux.append(self)

    def _get_num_local(self):
        return self._p_num_local

    def _set_num_local(self, v_num_local):
        if (v_num_local[0].isalpha().isupper() and v_num_local[1] == "-" and v_num_local[2, 3, 4].isdigit()
                and len(v_num_local) == 5):
            self._p_num_local = v_num_local

    num_local = property(_get_num_local, _set_num_local)

    def _get_dimension_local(self):
        return self._p_dimension_local

    def _set_dimension_local(self, v_dimension_local):
        if isinstance(v_dimension_local, float) and v_dimension_local > 0:
            self._p_dimension_local = v_dimension_local

    dimension_local = property(_get_dimension_local, _set_dimension_local)

    def _get_nb_places(self):
        return self._p_nb_places

    def _set_nb_places(self, v_nb_places):
        if isinstance(v_nb_places, int) and v_nb_places > 10:
            self._p_nb_places = v_nb_places

    nb_places = property(_get_nb_places, _set_nb_places)

    def __str__(self):
        return f"""Informations du local:
Type local: {self.type_local}
Lieu local: {self.lieu_local}
Dimension local: {self.dimension_local}m
Nb Places: {self.nb_places} places
"""