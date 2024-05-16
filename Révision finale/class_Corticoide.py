import class_Medicament as M

class Corticoide(M.Medicament):
    """
    Classe Corticoide qui hérite de la classe Médicament
    """
    def __init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie,
                 p_effet_medic: int = 0):
        """
        Constructeur de la classe Corticoide
        :param effet_medic: L'effet du médicament, court, intermédiaire ou prolongé
        """
        super().__init__(p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie)
        self.effet_medic = p_effet_medic

        M.Medicament.ls_medicaments.append(self)

    # Méthodes
    def __str__(self):
        return (f"Informations de l'analgésique:"
                f"Code du médicament: {self.code_medicament}"
                f"Nom chimique: {self.nom_chimique}"
                f"Nom commercial: {self.nom_commercial}"
                f"Prix: {self._prix}"
                f"Catégorie: {self.categorie}"
                f"Effet du médicament: {self.effet_medic}")