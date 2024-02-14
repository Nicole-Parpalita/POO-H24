class Rectangle:
    """
    Classe Rectangle
    """
    def __init__(self, p_l: float, p_L: float):
        """
        Constructeur de la classe Rectangle
        :param p_l: La longeur d'un rectangle
        :param p_L: La largeur d'un rectangle
        """
        self._longueur = p_l
        self._largeur = p_L

    def _get_longueur(self):
        if self._longueur > 0:
            return self._longueur
        else:
            return 1

    def _set_longueur(self, v_l: float):
        if v_l > 0:
            self._longueur = v_l

    longueur = property(_get_longueur, _set_longueur)

    def _get_largeur(self):
        if self._largeur > 0:
            return self._largeur
        else:
            return 1

    def _set_largeur(self, v_L: float):
        if v_L > 0:
            self._largeur = v_L

    largeur = property(_get_largeur, _set_largeur)