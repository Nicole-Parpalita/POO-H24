from Employe import Employe
from datetime import datetime

employe1 = Employe("2356641", "Parpalita", "Nicole", 1989, 35500.50, 2018)
employe2 = Employe("6673815", "Pimentel", "Jade", 1985, 48000.75, 2013)

def etablir_priorite(employe1: Employe, employe2: Employe) -> str:
    """
    Établit la priorité de stationnement gratuit entre 2 employés.
    """
    date_actuelle = datetime.now()
    annee_actuelle = int(date_actuelle.strftime("%Y"))

    # Ancienneté employé 1
    ancienneté1 = annee_actuelle - employe1.entree

    # Ancienneté employé 2
    ancienneté2 = annee_actuelle - employe2.entree

    if ancienneté1 > ancienneté2:
        return f"La priorité est à {employe1.prenom} {employe1.nom}."
    else:
        return f"La priorité est à {employe2.prenom} {employe2.nom}."

print(etablir_priorite(employe1, employe2))
Employe.afficher_information(employe1)
Employe.afficher_information(employe2)