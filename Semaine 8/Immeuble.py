import string


class Immeuble:
    """
    Classe Immeuble
    """
    # Attributs de classe
    nb_immeubles : int = 0
    dict_immeubles : dict = {}

    def __init__(self, p_id_immeuble : string = "", p_adresse : string = "", p_nb_appart : int = 0):
        """
        Constructeur de la classe Immeuble
        :param p_id_immeuble : L'ID de l'immeuble
        :param p_adresse : L'adresse de l'immeuble
        :param nb_appart : Le nombre d'appartements dans l'immeuble
        """
        # Attributs d'instances
        self._id_immeuble = p_id_immeuble
        self._adresse = p_adresse
        self._nb_appart = p_nb_appart
        Immeuble.nb_immeubles += 1
        Immeuble.dict_immeubles[self._id_immeuble] = self._adresse, self._nb_appart

        # Propriétés
        def _get_id_immeuble(self):
            return self._id_immeuble

        def _set_id_immeuble(self, v_id_immeuble):
            self._id_immeuble = v_id_immeuble

        id_immeuble = property(_get_id_immeuble, _set_id_immeuble)

        def _get_adresse(self):
            return self._adresse

        def _set_adresse(self, v_adresse):
            self._adresse = v_adresse

        adresse = property(_get_adresse, _set_adresse)

        def _get_nb_appart(self):
            return self._nb_appart

        def _set_nb_appart(self, v_nb_appart):
            self._nb_appart = v_nb_appart

        nb_appart = property(_get_nb_appart, _set_nb_appart)

        # Méthodes
