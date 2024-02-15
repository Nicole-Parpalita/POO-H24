"""
Programme qui permet de créer un compte
"""
class Compte:
    """
    Classe Compte
    """
    # Attribut de classe
    nb_comptes = 0
    def __init__(self, num_compte: str = "A123456789", nom_prenom_client: str = "", type_compte: str = "",
                 solde_compte: float = 0):
        """
        Constructeur de la classe Compte
        :param num_compte: Le numéro de compte qui doit être une chaîne de caractères alphanumériques (10 caractères)
        :param nom_prenom_client: Le nom et prénom du client
        :param type_compte: Le type de compte (chèque ou épargne)
        :param solde_compte: La solde du compte
        """
        # Assignation des valeurs en utilisant les propriétés pour appliquer les validations
        self._num_compte = num_compte
        self._nom_prenom_client = nom_prenom_client
        self._type_compte = type_compte
        self._solde_compte = solde_compte
        Compte.nb_comptes += 1

    # Propriété du numéro de compte
    def _get_num_compte(self):
        return self._num_compte

    def _set_num_compte(self, value):
        if isinstance(value, str) and len(value) == 10 and value.isalnum():
            self._num_compte = value
        else:
            raise ValueError("Le numéro de compte doit être alphanumérique et avoir une longueur de 10 caractères.")

    num_compte = property(_get_num_compte, _set_num_compte)

    # Propriété du nom et prénom du client
    def _get_nom_prenom_client(self):
        return self._nom_prenom_client

    def _set_nom_prenom_client(self, value):
        if (isinstance(value, str) and all(c.isalpha() or c in ["'", "-", " "] for c in value) and len(value) <= 50):
            self._nom_prenom_client = value
        else:
            raise ValueError("Le nom doit respecter les contraintes.")

    nom_prenom_client = property(_get_nom_prenom_client, _set_nom_prenom_client)

    # Propriété du type de compte du client
    def _get_type_compte(self):
        return self._type_compte

    def _set_type_compte(self, value):
        if isinstance(value, str) and value == "Chèque" or value == "Épargne":
            self._type_compte = value
        else:
            raise ValueError("Le type de compte ne peut être que chèque ou épargne.")

    type_compte = property(_get_type_compte, _set_type_compte)

    # Propriété du solder du compte
    def _get_solde_compte(self):
        return self._solde_compte

    def _set_solde_compte(self, value):
        if isinstance(value, float) and value >= 100:
            self._solde_compte = value
        else:
            raise ValueError("Le solde du compte doit être un chiffre et être au moins de 100$.")

    solde_compte = property(_get_solde_compte, _set_solde_compte)

    # Méthodes d'instance
    def afficher_informations(self) -> str:
        """
        Affiche les informations de l'instance
        :return: Les informations de l'instance
        """
        return f"""\nNuméro de compte               : {self._num_compte}
Nom du client                  : {self._nom_prenom_client}
Type de compte                 : {self._type_compte}
Solde du compte                : {self._solde_compte}"""

    def deposer(self, depot):
        """
        Déposer de l'argent dans le compte (ajouter au solde)
        :param depot: La quantité d'argent déposée dans le compte
        :return: Le nouveau solde
        """
        self._solde_compte += depot
        return self._solde_compte

    def retirer(self, retrait):
        """
        Retirer de l'argent du compte (dimunuer le solde)
        :param retrait: La quantité d'argent retirée du compte
        :return: Le nouveau solde
        """
        self._solde_compte -= retrait
        if self._solde_compte > 100:
            return self._solde_compte
        else:
            return ValueError

    def __str__(self):
        """
        Méthode magique
        :return: Une chaîne contenant les 4 dernies numéros du compte ainsi que le
        nom et prénom du propriétaire
        """
        return (f"\nLe propriétaire du compte est: {self._nom_prenom_client}.\n"
                f"""Les 4 derniers numéros du compte sont:{self._num_compte[6], self._num_compte[7], 
                self._num_compte[8], self._num_compte[9]}""")
