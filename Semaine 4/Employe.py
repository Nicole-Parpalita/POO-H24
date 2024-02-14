from datetime import datetime

class Employe:
    """
    Classe employé
    """
    def __init__(self, p_matricule="0000000", p_nom="Nom", p_prenom="Prenom", p_annee=1980, p_salaire=37500.50,
                 p_entree=2005):
        """
        Constructeur de la classe Employe
        :param p_matricule: La matricule de l'employé
        :param p_nom: Le nom de l'employé
        :param p_prenom: Le prénom de l'employé
        :param p_annee: L'année de naissance de l'employé
        :param p_salaire: Le salair annuel de l'employé
        :param p_entree: L'année d'entrée en fonction de l'employé
        """
        # Matricule
        for caractere in p_matricule:
            if caractere.isdigit() and len(p_matricule) == 7:
                self._matricule = p_matricule

        # Nom
        if len(p_nom) < 50:
            self._nom = p_nom

        # Prénom
        if len(p_prenom) < 50:
            self._prenom = p_prenom

        # Année de naissance
        if isinstance(p_annee, int):
            self._annee = p_annee

        # Salaire annuel
        if isinstance(p_salaire, float):
            self._salaire = p_salaire

        # Année d'entrée en fonction
        if isinstance(p_entree, int):
            self._entree = p_entree


    # MATRICULE
    def _get_matricule(self) -> str:
        return self._matricule

    def _set_matricule(self, p_matricule: str):
        self._matricule = p_matricule

    matricule = property(_get_matricule, _set_matricule)


    # NOM
    def _get_nom(self) -> str:
        return self._nom

    def _set_nom(self, p_nom) -> str:
        self._nom = p_nom

    nom = property(_get_nom, _set_nom)


    # PRÉNOM
    def _get_prenom(self) -> str:
        return self._prenom

    def _set_prenom(self, p_prenom: str):
        self._prenom = p_prenom

    prenom = property(_get_prenom, _set_prenom)


    # ANNÉE DE NAISSANCE
    def _get_annee(self) -> int:
        return self._annee

    def _set_annee(self, p_annee: int):
        self._annee = p_annee

    annee = property(_get_annee, _set_annee)


    # SALAIRE ANNUEL
    def _get_salaire(self) -> float:
        return self._salaire

    def _set_salaire(self, p_salaire: float):
        self._salaire = p_salaire

    salaire = property(_get_salaire, _set_salaire)


    # ANNÉE D'ENTRÉE
    def _get_entree(self) -> int:
        return self._entree

    def _set_entree(self, p_entree: int):
        self._entree = p_entree

    entree = property(_get_entree, _set_entree)



    # MÉTHODES
    # AFFICHER LES INFORMATIONS DE L'EMPLOYÉ
    def afficher_information(self):
        """
        Affiche les informations de l'employé
        """
        date_actuelle = datetime.now()
        annee_actuelle = int(date_actuelle.strftime("%Y"))

        # AGE
        age = annee_actuelle - self._annee

        # ANCIENNETÉ
        anciennete = annee_actuelle - self._entree

        # DROIT STATIONNEMENT
        droit_stationnement = ""
        if age > 40 and anciennete > 20:
            droit_stationnement = True
        else:
            droit_stationnement = False

        # CATÉGORIE SALAIRE
        classe_salaire = ""
        if 25000 <= self._salaire <= 35000:
            classe_salaire = "A"
        elif 35000 <= self._salaire <= 45000:
            classe_salaire = "B"
        elif 45000 <= self._salaire <= 70000:
            classe_salaire = "C"
        else:
            classe_salaire = "F"

        # AFFICHER INFOS
        print(f"""La matricule de l'employé est {self._matricule}.
Le nom et prénom de l'employé est {self._nom} {self._prenom}.
L'année de naissance de l'employé est {self._annee}.
Le salaire annuel de l'employé est {self._salaire:.2f} $.
L'année d'entrée en fonction de l'employé est {self._entree}.
L'âge de l'employé est {age} ans.
L'ancienneté de l'employé est de {anciennete} années.
Cet employé à le droit au stationnement gratuit: {droit_stationnement}.
La classe de salaire de cet employé est de {classe_salaire}.
""")





























