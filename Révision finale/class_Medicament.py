class Medicament:
    """
    Classe Medicament
    """
    # Attributs de classe
    ls_medicaments = []
    nb_medicaments = 0

    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "",
                 p_nom_commercial: str ="", p_prix: float = 0.0, p_categorie: str = ""):
        """
        Constructeur de la classe Medicament
        :param p_code_medicament: Le code du médicament
        :param p_nom_chimique: Le nom chimique du médicament
        :param p_nom_commercial: Le nom commercial du médicament
        :param p_prix: Le prix du médicament
        :param p_categorie: La catégorie du médicament
        """
        self._code_medicament = p_code_medicament
        self._nom_chimique = p_nom_chimique
        self._nom_commercial = p_nom_commercial
        self._prix = p_prix
        self.categorie = p_categorie

        Medicament.ls_medicaments.append(self)
        Medicament.nb_medicaments += 1

    # Propriétés
    def _get_code_medicament(self):
        return self._code_medicament

    def _set_code_medicament(self, v_code_medicament: str):
        if len(v_code_medicament) == 6 and v_code_medicament[0:2].isalpha() and v_code_medicament[3:].isnumeric():
            self._code_medicament = v_code_medicament
        else:
            raise ValueError("Le code de médicament doit être composé de trois lettres suivies de 3 chiffres.")

    code_medicament = property(_get_code_medicament, _set_code_medicament)

    def _get_nom_chimique(self):
        return self._nom_chimique

    def _set_nom_chimique(self, v_nom_chimique: str):
        if isinstance(v_nom_chimique, str) and len(v_nom_chimique) <= 50:
            self._nom_chimique = v_nom_chimique
        else:
            raise ValueError("Le nom chimique doit être composé d'un maximum de 50 caractères.")

    nom_chimique = property(_get_nom_chimique, _set_nom_chimique)

    def _get_nom_commercial(self):
        return self._nom_commercial

    def _set_nom_commercial(self, v_nom_commercial: str):
        if isinstance(v_nom_commercial, str) and len(v_nom_commercial) <= 50:
            self._nom_commercial = v_nom_commercial
        else:
            raise ValueError("Le nom commercial doit être composé d'un maximum de 50 caractères.")

    nom_commercial = property(_get_nom_commercial, _set_nom_commercial)

    def _get_prix(self):
        return self._prix

    def _set_prix(self, v_prix: float):
        if isinstance(v_prix, float) and v_prix <= 100 and v_prix >= 5:
            self._prix = v_prix
        else:
            raise ValueError("Le prix doit avoir une valeur entre 5$ et 100$.")

    prix = property(_get_prix, _set_prix)

    # Méthodes
    def __str__(self):
        """
        Méthode magique qui permet d'afficher les informations du médicament
        """
        return (f"Informations du médicament:"
                f"Code du médicament: {self.code_medicament}"
                f"Nom chimique: {self.nom_chimique}"
                f"Nom commercial: {self.nom_commercial}"
                f"Prix: {self._prix}"
                f"Catégorie: {self.categorie}")

    def __add__(self, prix2: float):
        """
        Méthode magique qui permet d'ajouter le prix de deux médicaments
        """
        return self.prix + prix2