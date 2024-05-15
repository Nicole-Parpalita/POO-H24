import datetime
from class_Medicament import Medicament
import re

class Patient:
    """
    Classe Patient
    """
    # Attributs de classe
    ls_patients = []
    nb_patients = 0

    def __init__(self, p_num_patient: int = 0, p_nom: str = "", p_prenom: str = "",
                 p_date_naissance: datetime = None, p_adresse_courriel: str = "", p_ls_medic: list[Medicament] = None):
        """
        Constructeur de la classe Patient
        :param p_num_patient: Le numéro de patient
        :param p_nom: Le nom du patient
        :param p_prenom: Le prénom du patient
        :param p_date_naissance: La date de naissance du patient
        :param adresse_courriel: L'adresse courriel du patient
        """
        self._num_patient = p_num_patient
        self._nom = p_nom
        self._prenom = p_prenom
        self._date_naissance = p_date_naissance
        self._adresse_courriel = p_adresse_courriel
        self._ls_medic = p_ls_medic

    # Propriétés
    def _get_num_patient(self):
        return self._num_patient

    def _set_num_patient(self, v_num_patient: int):
        if isinstance(v_num_patient, int) and len(v_num_patient) == 7 and v_num_patient[0] in [0, 2, 4, 6, 8]:
            self._num_patient = v_num_patient
        else:
            raise ValueError("Le numéro de patient doit être composé de 7 chiffres dont le premier est pair.")

    num_patient = property(_get_num_patient, _set_num_patient)

    def _get_nom(self):
        return self._nom

    def _set_nom(self, v_nom: str):
        if isinstance(v_nom, str) and len(v_nom) <= 50:
            self._nom = v_nom
        else:
            raise ValueError("Le nom doit être composé d'un maximum de 50 caractères.")

    nom = property(_get_nom, _set_nom)

    def _get_prenom(self):
        return self._prenom

    def _set_prenom(self, v_prenom: str):
        if isinstance(v_prenom, str) and len(v_prenom) <= 50:
            self._prenom = v_prenom
        else:
            raise ValueError("Le prénom doit être composé d'un maximum de 50 caractères.")

    prenom = property(_get_prenom, _set_prenom)

    def _get_date_naissane(self):
        return self._date_naissance

    def _set_date_naissance(self, v_date_naissance: datetime):
        if isinstance(v_date_naissance, datetime):
            self._date_naissance = v_date_naissance

    date_naissance = property(_get_date_naissane, _set_date_naissance)

    def _get_adresse_courriel(self):
        return self._adresse_courriel

    def _set_adresse_courriel(self, v_adresse_courriel: str):
        modele = r'^[a-zA-Z]+\.[a-zA-Z]+@gmail\.com$'
        if re.match(modele, v_adresse_courriel):
            self._adresse_courriel = v_adresse_courriel
        else:
            raise ValueError("L'adresse courriel ne respecte pas le format requis du nom "
                             "suivi du prénom suivi de @gmail.com.")

    adresse_courriel = property(_get_adresse_courriel, _set_adresse_courriel)


    def _get_ls_medic(self):
        return self._ls_medic

    def _set_ls_medic(self, v_ls_medic: list[Medicament]):
        if isinstance(v_ls_medic, list[Medicament]):
            self._ls_medic = v_ls_medic

    ls_medic = property(_get_ls_medic, _set_ls_medic)

    # Méthodes
    def calculer_age(self):
        """
        Calcule l'âge d'un patient
        :param v_date_naissance: La date de naissance du patient (doit être un objet datetime.date)
        :return: Retourne l'âge du patient
        """
        ajd = datetime.date.today()
        age = ajd.year - self.date_naissance.year - ((ajd.month, ajd.day) < (self.date_naissance.month,
                                                                             self.date_naissance.day))
        return age

    def estAdulte(self) -> bool:
        """
        Vérifie si le patient a plus ou moins que 18 ans
        :param age: L'âge du patient
        :return: True si le patient a dépassé 18 ans et False si non
        """
        age = self.calculer_age()
        return age >= 18

    def afficherMedicaments(self):
        """
        Affiche de façon professionnelle les attributs de la liste de médicaments du patient
        """
        for med in self._ls_medic:
            print(f"Voici les médicaments achetés par le patient {self.num_patient}:")
            print("*" * 30)
            print(f"Code du médicament: {self.code_medicament}"
                f"Nom chimique: {self.nom_chimique}"
                f"Nom commercial: {self.nom_commercial}"
                f"Prix: {self._prix}"
                f"Catégorie: {self.categorie}")
            print("*" * 30)

    def ajouterMedicament(self, medicament: Medicament):
        """
        Ajoute à la liste de médicaments du patient un objet de type Medicament
        :param medicament: Le médicament à ajouter
        """
        self.ls_medic.append(medicament)

    def supprimerMedicament(self, medicament: Medicament):
        """
        Supprime de la liste de médicaments du patient un objet
        :param medicament: Le médicament à supprimer
        """
        if medicament in self.ls_medic:
            self.ls_medic.remove(medicament)
        else:
            print("Le médicament n'existe pas dans la liste de médicaments du patient.")

