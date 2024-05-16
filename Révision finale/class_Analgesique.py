import class_Medicament as M

class Analgesique(M.Medicament):
    """
    Classe Analgesique qui hérite de la classe Médicament
    """
    def __init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie,
                 p_dose_quot_max: int = 0):
        """
        Constructeur de la classe Analgesique
        :param p_dose_quot_max: La dose quotidienne maximale qui est en nombre de comprimés
        """
        super().__init__(p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie)
        self._dose_quot_max = p_dose_quot_max

        M.Medicament.ls_medicaments.append(self)

    # Propriétés
    def _get_dose_quot_max(self):
        return self._dose_quot_max

    def _set_dose_quot_max(self, v_dose_quot_max):
        if isinstance(v_dose_quot_max, int) and v_dose_quot_max > 0:
            self._dose_quot_max = v_dose_quot_max
        else:
            raise ValueError("La dose quotidienne maximale doit être en nombre de comprimés.")

    dose_quot_max = property(_get_dose_quot_max, _set_dose_quot_max)

    # Méthodes
    def __str__(self):
        return (f"Informations de l'analgésique:"
                f"Code du médicament: {self.code_medicament}"
                f"Nom chimique: {self.nom_chimique}"
                f"Nom commercial: {self.nom_commercial}"
                f"Prix: {self._prix}"
                f"Catégorie: {self.categorie}"
                f"Dose quotidienne maximale: {self.dose_quot_max}")