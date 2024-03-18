class Appartement:
    """
    Classe Appartement
    """
    # Attributs de classe
    nb_apparts : int = 0
    ls_loyers : list = []
    dict_apparts : dict = {}
    ls_apparts = list = []
    def __init__(self, p_numero_appart : int = 0, p_balcon : bool = True, p_nb_chambres : int = 0,
                 p_loyer : float = 0.0, p_ls_apparts: list = [], p_nb_apparts : int = 0):
        """
        Constructeur de la classe Appartement
        :param p_numero_appart : Le numéro de l'appartement
        :param p_balcon : S'il y a ou non un appartement
        :param p_nb_chambres : Le nombre de chambres
        :param p_loyer : Le loyer de l'appartement
        """
        # Attributs d'instances
        self._numero_appart = p_numero_appart
        self._balcon = p_balcon
        self._nb_chambres = p_nb_chambres
        self._loyer = p_loyer
        self._ls_apparts = p_ls_apparts
        self._nb_apparts = p_nb_apparts
        Appartement.nb_apparts += 1
        Appartement.ls_loyers.append(p_loyer)
        Appartement.dict_apparts[self._numero_appart] = self._balcon, self._nb_chambres, self._loyer

        # Propriétés
        def _get_numero_appart(self):
            return self._numero_appart

        def _set_numero_appart(self, v_numero_appart):
            self._numero_appart = v_numero_appart

        numero_appart = property(_get_numero_appart, _set_numero_appart)

        def _get_balcon(self):
            return self._balcon

        def _set_balcon(self, v_balcon):
            self._balcon = v_balcon

        balcon = property(_get_balcon, _set_balcon)

        def _get_nb_chambres(self):
            return self._nb_chambres

        def _set_nb_chambres(self, v_nb_chambres):
            self._nb_chambres = v_nb_chambres

        nb_chambres = property(_get_nb_chambres, _set_nb_chambres)

        def _get_loyer(self):
            return self._loyer

        def _set_loyer(self, v_loyer):
            self._loyer = v_loyer

        loyer = property(_get_loyer, _set_loyer)

        def _get_nb_apparts(self):
            return self._loyer

        def _set_loyer(self, v_loyer):
            self._loyer = v_loyer

        loyer = property(_get_loyer, _set_loyer)



        # Méthodes


