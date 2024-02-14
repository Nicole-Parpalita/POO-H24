class Livre:
    """
    Classe Livre
    """
    def __init__(self, p_titre: str, p_auteur: str, p_prix: float):
        """
        Constructeur de la classe Livre
        :param titre: Le titre du livre
        :param auteur: L'auteur du livre
        :param prix: Le prix du livre
        """
        self._titre = p_titre
        self._auteur = p_auteur
        if p_prix > 0:
            self._prix = p_prix
        else:
            self._prix = 1

    def _get_titre(self) -> str:
        return self._titre

    def _set_titre(self, p_titre: str):
        self._titre = p_titre

    titre = property(_get_titre, _set_titre)

    def _get_auteur(self) -> str:
        return self._auteur

    def _set_auteur(self, p_auteur: str):
        self._auteur = p_auteur

    auteur = property(_get_auteur, _set_auteur)

    def _get_prix(self) -> float:
        return self._prix

    def _set_prix(self, p_prix: float):
        if p_prix > 0:
            self._prix = p_prix
        else:
            self._prix = 1

    prix = property(_get_prix, _set_prix)

    def afficher_informations(self):
        """
        Affiche les informations du livre
        :return: None
        """
        print("Le titre du livre est", self._titre)
        print("L'auteur du livre est", self._auteur)
        print("Le prix du livre est", self._prix, "$")