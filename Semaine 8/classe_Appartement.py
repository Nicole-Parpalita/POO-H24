class Appartement:
    """
    Classe Appartement
    """
    # Attributs de classe
    nb_apparts = 0
    ls_apparts = []

    def __init__(self, p_num_appart: string = "", p_balcon: bool = True, p_nb_chambres: int = 0,
                 p_ls_locataires: list[Locataire] = None, p_immeuble: Immeuble = None):
        """
        Constructeur de la classe Appartement
        :param p_num_appart: Le numéro de l'appart
        :param p_balcon: Si l'appart possède un balcon ou non
        :param p_nb_chambres: Le nombre de chambres dans l'appart
        :param p_ls_locataires: La liste des locataires de l'appart
        :param p_immeuble: L'immeuble de l'appart
        """
        self.num_appart = p_num_appart
        self.balcon = p_balcon
        self.nb_chambres = p_nb_chambres
        if p_ls_locataires is None:
            self.ls_locataires = []
        else:
            self.ls_locataires = p_ls_locataires
        self.immeuble = p_immeuble

    # Propriétés
    # Méthodes
    def verifier_appart_liste(self):
        """
        Vérifier si un appartement instancié existe déjà dans la liste d'apparts
        :return: True si l'appart existe, False si non
        """
        for appart in Appartement.ls_apparts:
            if self.num_appart == app.num_appart:
                return True
            else:
                return False

    def ajouter_appart(self):
        """
        Ajouter un appartement à la liste de classe des appartements
        :return: True si l'ajout a réussi, False si non
        """
        if self.verifier_appart_liste() is False:
            Appartement.ls_apparts.append(self)
            return True
        else:
            return False

    @classmethod
    def retourner_nb_appart_liste(cls):
        """
        Retourner le nombre d'appartements de la liste
        :return: Le nombre d'apparts de la liste
        """
        return len(cls.ls_apparts)

    @classmethod
    def retourner_nb_appart(cls):
        """
        Retourner le nombre d'apparts instanciés
        :return: Le nombre d'apparts instanciés
        """
        return cls.nb_apparts

    @classmethod
    def retourner_appart_balcon(cls):
        """
        Retourner les appartements qui possèdent des balcons
        :return: La liste des appartements avec balcon
        """
        ls_apparts_balcons = []
        for appart in cls.ls_apparts:
            if appart.balcon is True:
                ls_apparts_balcons.append(appart)
            else:
                pass
        return ls_apparts_balcons

    @staticmethod
    def calculer_loyer(p_loyer_mensuel: float, nb_mois: int):
        """
        Calculer le loyer du locataire de l'appartement
        :return: Le loyer
        """
        return p_loyer_mensuel * (nb_mois - 1)