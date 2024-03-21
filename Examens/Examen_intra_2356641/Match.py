class Match:
    """
    Classe Match
    """
    def __init__(self, p_code_match: string = ""):
        """
        Constructeur de la classe Match
        :param p_code_match: Le code du match
        """
        self.code_match = p_code_match

    # Méthodes
    def __str__(self):
        """
        Méthode magique
        :return: Une chaîne contenant le code du match
        """
        return f"Le code de ce match est : {self.code_match}."