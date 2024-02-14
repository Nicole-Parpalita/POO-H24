class Voiture:
    def __init__(self):
        self._roues = 4

    def _get_roues(self):
        print("Récupération du nombre de roues")
        return self._roues

    def _set_roues(self, v):
        print("Changement du nombre des roues")
        self._roues = v

    roues = property(_get_roues, _set_roues)

