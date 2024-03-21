from JoueurSoccer import JoueurSoccer
from Equipe import Equipe

joueur1 = JoueurSoccer(33, "Félix")
joueur2 = JoueurSoccer(12, "Mathis")
joueur3 = JoueurSoccer(99, "Nic")
equipe1 = Equipe("12345", "Cyclones", [joueur1, joueur2, joueur3])

Equipe.afficher_joueurs(equipe1)