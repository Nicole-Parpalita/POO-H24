from Livre import Livre
from Auteur import Auteur

livre1 = Livre("1234567891231", "Harry Potter", [auteur1, auteur2])
livre2 = Livre("0000000000000", "Horry Patter")
auteur1 = Auteur("123456", "Rowling", "J.K.", [livre1, livre2])
auteur2 = Auteur("000000", "Nicole", "Parpalita", [livre1])


# print(livre1.auteur.retourner_infos_auteur())
# print(livre1.auteur)

print(livre1.ls_auteurs)

