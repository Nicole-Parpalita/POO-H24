from class_Patient import Patient
import jsonpickle
from class_Medicament import Medicament

class Fournisseur:
    """
    Classe Fournisseur
    """
    # Attributs de classe
    ls_fournisseurs = []
    nb_fournisseurs = 0

    def __init__(self, p_code_fournisseur: str = "", p_nom_compagnie: str = "", p_ls_patients: list[Patient] = None):
        """
        Constructeur de la classe Fournisseur
        :param p_code_fournisseur: Le code du fournisseur
        :param nom_compagnie: Le nom de la compagnie du fournisseur
        :param ls_patients: La liste de patients associés à ce fournisseur
        """
        self._code_fournisseur = p_code_fournisseur
        self._nom_compagnie = p_nom_compagnie
        self._ls_patients = p_ls_patients

        Fournisseur.ls_fournisseurs.append(self)
        Fournisseur.nb_fournisseurs += 1

    # Propriétés
    def _get_code_fournisseur(self):
        return self._code_fournisseur

    def _set_code_fournisseur(self, v_code_fournisseur: str):
        if isinstance(v_code_fournisseur, str) and len(v_code_fournisseur) == 6 and v_code_fournisseur[0] == "F" and v_code_fournisseur[1:4].isnumeric():
            self._code_fournisseur = v_code_fournisseur
        else:
            raise ValueError("Le code fournisseur doit être composé d'un F majuscule suivi de 5 chiffres.")

    code_fournisseur = property(_get_code_fournisseur, _set_code_fournisseur)

    def _get_nom_compagnie(self):
        return self._nom_compagnie

    def _set_nom_compagnie(self, v_nom_compagnie: str):
        if isinstance(v_nom_compagnie, str) and len(v_nom_compagnie) <= 30 and v_nom_compagnie.isalnum():
            self._nom_compagnie = v_nom_compagnie
        else:
            raise ValueError("Le nom de la compagnie doit être composé d'un maximum de 30 caractères.")

    nom_compagnie = property(_get_nom_compagnie, _set_nom_compagnie)

    def _get_ls_patients(self):
        return self._ls_patients

    def _set_ls_patients(self, v_ls_patients: list[Patient]):
        if isinstance(v_ls_patients, list[Patient]):
            self._ls_patients = v_ls_patients

    ls_patients = property(_get_ls_patients, _set_ls_patients)

    # Méthodes
    def serialiserFournisseur(self, p_fichier):
        """
        Permet de sérialiser un objet de type Fournisseur vers un fichier json
        """
        with open(p_fichier, "w") as F:
            F.write(jsonpickle.encode(self))

    def deserialiserFournisseur(self, p_fichier):
        """
        Permet de désérialiser un fichier json en un objet de type Fournisseur
        """
        with open(p_fichier, "r") as F:
            dataFournisseur = F.read()
        ObjFournisseur = jsonpickle.decode(dataFournisseur)
        return ObjFournisseur

    def ajouterMedicamentPatient(self, num_patient: int, medicament: Medicament):
        """
        Permet de chercher un patient dans la liste de patients et de lui ajouter un médicament
        :param num_patient: Le numéro du patient à chercher
        :param medicament: Le médicament à ajouter au patient
        """
        for patient in self.ls_patients:
            if patient.num_patient == num_patient:
                patient.ajouterMedicament(medicament)

    @classmethod
    def afficherLstFournisseurs(cls):
        """
        Permet d'afficher la liste des fournisseurs de façon professionnelle
        """
        print(f"Voici la liste des fournisseurs:")
        for fournisseur in cls.ls_fournisseurs:
            print(f"Code fournisseur: {fournisseur.code_fournisseur}"
                  f"Nom de compagnie: {fournisseur.nom_compagnie}"
                  f"************************************************")

    def __str__(self):
        """
        Méthode magique qui permet d'afficher les informations du fournisseur
        """
        return(f"Code fournisseur: {self.code_fournisseur}"
              f"Nom de compagnie: {self.nom_compagnie}")