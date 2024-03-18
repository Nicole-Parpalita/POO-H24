from datetime import date


class Locataire:
    """
    Classe Locataire
    """
    # Attributs de classe
    nb_locataires : int = 0
    dict_locataire : dict = {}

    def __init__(self, p_id_locataire: string = "", p_num_compte : string = "", p_num_appart : int = 0,
                 p_date_location : date = Default(date)):
        """
        Constructeur de la classe Locataire
        :param p_id_locataire: L'ID du locataire
        :param p_num_compte: Le numéro de compte bancaire du locataire
        :param num_appart: Le numéro de l'appartement du locataire
        :param date_location: La date de location du locataire
        """
        self._id_locataire = p_id_locataire
        self._num_compte = p_num_compte
        self._num_appart = p_num_appart
        self._date_location = p_date_location
        Locataire.nb_locataires += 1
        Locataire.dict_locataire[self._id_locataire] = self._num_compte, self._num_appart, self._date_location