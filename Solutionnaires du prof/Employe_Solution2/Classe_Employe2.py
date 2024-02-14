"""
Programme qui permet d'entrer des employés
"""
from datetime import datetime


class Employe:
    """
    Classe Employe
    """
    def __init__(self, matricule: str = "1234567", nom: str = "X", prenom: str = "X",
                 annee_naissance: int = 2000, salaire_annuel: float = 20000.0, annee_entree_fonction: int = 2018):

        """
        Constructeur de la classe Employe
        :param matricule: matricule de l'employé
        :param nom: nom de l'employé
        :param prenom: prénom de l'employé
        :param annee_naissance: année de naissance de l'employé
        :param salaire_annuel: salaire annuel de l'employé
        :param annee_entree_fonction: fonction de l'employé
        """
        # Assignation des valeurs en utilisant les propriétés pour appliquer les validations
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.annee_naissance = annee_naissance
        self.salaire_annuel = salaire_annuel
        self.annee_entree_fonction = annee_entree_fonction

    # Propriété matricule
    def _get_matricule(self):
        return self._matricule

    def _set_matricule(self, value):
        if isinstance(value, str) and len(value) == 7 and value.isdigit():
            self._matricule = value
        else:
            raise ValueError("Le matricule doit être une chaîne de sept chiffres.")

    matricule = property(_get_matricule, _set_matricule)

    # Propriété nom
    def _get_nom(self):
        return self._nom

    def _set_nom(self, value):
        if isinstance(value, str) and all(c.isalpha() or c in ["'", "-", " "] for c in value) and len(value) <= 50:
            self._nom = value
        else:
            raise ValueError("Le nom doit être une chaîne composée de caractères alphabétiques, d'apostrophes, "
                             "de tirets ou d'espaces, et de longueur inférieure ou égale à 50.")

    nom = property(_get_nom, _set_nom)

    # Propriété prenom
    def _get_prenom(self):
        return self._prenom

    def _set_prenom(self, value):
        if isinstance(value, str) and all(c.isalpha() or c in ["'", "-", " "] for c in value) and len(value) <= 50:
            self._prenom = value
        else:
            raise ValueError("Le prénom doit être une chaîne composée de caractères alphabétiques, d'apostrophes, "
                             "de tirets ou d'espaces, et de longueur inférieure ou égale à 50.")

    prenom = property(_get_prenom, _set_prenom)

    # Propriété annee_naissance
    def _get_annee_naissance(self):
        return self._annee_naissance

    def _set_annee_naissance(self, value):
        current_year = datetime.now().year
        # L'âge de l'employé doit être entre 18 et 60 ans
        if isinstance(value, int) and current_year - 60 <= value <= current_year - 18:
            self._annee_naissance = value
        else:
            raise ValueError("L'année de naissance doit être un entier et l'âge de l'employé ne doit pas "
                             "dépasser 60 ans.")

    annee_naissance = property(_get_annee_naissance, _set_annee_naissance)

    # Propriété salaire_annuel
    def _get_salaire_annuel(self):
        return self._salaire_annuel

    def _set_salaire_annuel(self, value):
        if isinstance(value, (int, float)) and 20000 <= value <= 70000:
            self._salaire_annuel = value
        else:
            raise ValueError("Le salaire annuel doit être un nombre positif.")

    salaire_annuel = property(_get_salaire_annuel, _set_salaire_annuel)

    # Propriété annee_entree_fonction
    def _get_annee_entree_fonction(self):
        return self._annee_entree_fonction

    def _set_annee_entree_fonction(self, value):
        current_year = datetime.now().year
        # L'employé ne peut pas travailler plus de 42 ans (de 18 ans à 60 ans)
        if (isinstance(value, int) and 0 <= current_year - value <= 42 and
                current_year - value <= self.calculer_age() - 18):
            self._annee_entree_fonction = value
        else:
            raise ValueError("L'année d'entrée en fonction doit être supérieure à la date actuelle moins 45 ans.")

    annee_entree_fonction = property(_get_annee_entree_fonction, _set_annee_entree_fonction)

    # Méthodes d'instance
    def afficher_informations(self):
        """
        Affiche les informations de l'instance
        :return: None
        """
        print(f"Matricule: {self.matricule}")
        print(f"Nom: {self.nom}")
        print(f"Prénom: {self.prenom}")
        print(f"Année de naissance: {self.annee_naissance}")
        print(f"Salaire annuel: {self.salaire_annuel}")
        print(f"Année d'entrée en fonction: {self.annee_entree_fonction}")

    def calculer_age(self):
        """
        Permet de calculer l'âge de l'employé
        :return: l'âge de l'employé
        """
        current_year = datetime.now().year
        return current_year - self.annee_naissance

    def calculer_anciennete(self):
        """
        Calcule l'ancienneté de l'employé
        :return: l'ancienneté de l'employé
        """
        current_year = datetime.now().year
        return current_year - self.annee_entree_fonction

    def calculer_droit_stationnement_gratuit(self):
        """
        Détermine si l'employé a droit au stationnement gratuit en fonction de son
        âge et son ancienneté
        :return: True si l'employé a le droit au stationnement gratuit
        False sinon.
        """
        if self.calculer_age() > 40 or self.calculer_anciennete() > 20:
            return True
        else:
            return False
        
    def calculer_categorie_salaire(self):
        """
        Détermine la catégorie de l'employé en fonction son salaire
        :return: La catégorie de l'employé
        """
        if 25000 <= self.salaire_annuel <= 35000:
            return 'A'
        elif 35000 < self.salaire_annuel <= 45000:
            return 'B'
        elif 45000 < self.salaire_annuel <= 70000:
            return 'C'
        else:
            return 'Indéterminé'


    def __str__(self):
        """
        Méthode magique
        :return: chaîne contenant des informations sur l'instance d'objet
        """
        return (f"\nLe matricule de l'employé est {self._matricule}\n"
                f"Le nom de l'employé est : {self._nom}\n"
                f"Le prénom de l'employé est : {self._prenom}\n"
                f"L'année de naissance de l'employé est {self._annee_naissance}\n"
                f"Le salaire annuel de l'employé est {self._salaire_annuel}\n"
                f"La date d'entrée en fonction {self._annee_entree_fonction}\n")


