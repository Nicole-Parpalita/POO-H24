from Livre import Livre
from Auteur import Auteur

auteur1 = Auteur("123456", "Rowling", "J.K.")
livre1 = Livre("1234567891231", "Harry Potter", auteur1)
print(livre1.isbn, livre1.titre, livre1.auteur.nom, livre1.auteur.prenom)

