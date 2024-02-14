class Point:
    """
    Classe Point
    """
    def __init__(self, p_x: int, p_y: int):
        """
        Constructure de la classe Point
        :param p_x: x
        :param p_y: y
        """
        self._x = p_x
        self._y = p_y

    def _get_x(self):
        if self._x < 100:
            return self._x
        else:
            return 0

    def _set_x(self, v_x: int):
        if v_x > 0 : self._x = v_x

    x = property(_get_x, _set_x)

    def _get_y(self):
        if self._y < 100:
            return self._y
        else :
            return 0

    def _set_y(self, v_y: int):
        if v_y > 0 : self._y = v_y

    y = property(_get_y, _set_y)


    def afficher_informations(self):
        """
        Affiche les informations des points
        :return: None
        """
        print("La valeur de x est", self._x)
        print("Le valeur de y est", self._y)