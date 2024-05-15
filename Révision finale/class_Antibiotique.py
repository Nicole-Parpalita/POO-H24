import class_Medicament as M

class Antibiotique(M.Medicament):
    """
    Classe Antibiotique qui hérite de la classe Médicament
    """
    def __init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie,
                 p_duree_prise_max: int = 0):
        """
        Constructeur de la classe Antibiotique
        :param p_duree_prise_max: La durée de prise maximale qui est en nombre de jours
        """
        super().__init__(p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie)
        self._duree_prise_max = p_duree_prise_max

    # Propriétés
    def _get_duree_prise_max(self):
        return self._duree_prise_max

    def _set_duree_prise_max(self, v_duree_prise_max):
        if isinstance(v_duree_prise_max, int) and v_duree_prise_max > 0:
            self._duree_prise_max = v_duree_prise_max
        else:
            raise ValueError("La durée de prise maximale doit être en nombre de jours.")

    duree_prise_max = property(_get_duree_prise_max, _set_duree_prise_max)

    # Méthodes
    def __str__(self):
        return (f"Informations de l'antibiotique:"
                f"Code du médicament: {self.code_medicament}"
                f"Nom chimique: {self.nom_chimique}"
                f"Nom commercial: {self.nom_commercial}"
                f"Prix: {self._prix}"
                f"Catégorie: {self.categorie}"
                f"Durée de prise maximale: {self.duree_prise_max}")