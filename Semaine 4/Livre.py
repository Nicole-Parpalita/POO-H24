class Livre:
    """
    Classe Livre
    """
    # Attribut de classe
    nb_livres = 0
    _ls_livres = []
    def __init__(self, id_unique: str = "XXXXXXXXXXXXX", titre: str = "", auteur: str = "",
                 annee_publication: int = 2000, disponible: bool = True):
        """
        Constructeur de la classe Livre
        :param id_unique: L'ISBN du livre
        :param titre: Titre du livre
        :param auteur: Auteur du livre
        :param annee_publication: Année de publication du livre
        :param disponible: True si le livre est disponible, False si non
        """

        # Assignation des valeurs en utilisant les propriétés pour appliquer les validations
        self._id_unique = id_unique
        self._titre = titre
        self._auteur = auteur
        self._annee_publication = annee_publication
        self._disponible = True
        Livre.nb_livres += 1
        Livre._ls_livres.append(self)

        # Propriété de l'ISBN
        def _get_id_unique(self):
            return self._id_unique

        def _set_id_unique(self, value):
            if (isinstance(value, str)) and (len(value) == 13) and value.isdigit():
                self._id_unique = value

        id_unique = property(_get_id_unique, _set_id_unique)

        # Propriété du titre
        def _get_titre(self):
            return self._titre

        def _set_titre(self, value):
            if isinstance(value, str) and all(c.isalpha() or c in ["'", "-", " "] for c in value):
                self._titre = value

        titre = property(_get_titre, _set_titre)

        # Propriété de l'auteur
        def _get_auteur(self):
            return self._auteur

        def _set_auteur(self, value):
            if isinstance(value, str) and all(c.isalpha() or c in ["'", "-", " "] for c in value):
                self._titre = value

        auteur = property(_get_auteur, _set_auteur)

        # Propriété de l'année de publication
        def _get_annee_publication(self):
            return self._annee_publication

        def _set_annee_publication(self, value):
            if isinstance(value, int) and value >= 0:
                self._annee_publication = value

        annee_publication = property(_get_annee_publication, _set_annee_publication)

        # Méthodes d'instance
        def emprunter(self):
            """
            Change la disponibilité du livre
            """
            if self._disponible:
                print(f"Le livre '{self._titre}' a été emprunté.")
                self._disponible = False
            else:
                print(f"Le livre '{self._titre}' n'est pas disponible.")

        def retourner(self):
            self._disponible = True
            return self._disponible

        def afficher_nombre_livres(self):
            return f"Le nombre de livres instanciés est de {Livre.nb_livres}."


        def __str__(self):
            """
            Méthode magique
            :return: Chaîne contenant des informations sur l'instance d'objet
            """
            return (f"\nL'ISBN du livre est : {self.id_unique}\n"
                    f"Le titre du livre est : {self._nom}\n"
                    f"L'auteur du livre est : {self._prenom}\n"
                    f"L'année de publication du livre est : {self._annee_naissance}\n")
