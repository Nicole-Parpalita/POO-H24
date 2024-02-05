from Voiture import Voiture

# Instrancier trois objets de la classe voiture
ma_voiture = Voiture("Ferrari", "XXX")
ta_voiture = Voiture("Toyota", "Matrix")
voiture_Daniel =Voiture("Honda", "Civic")

# Afficher les attributs des objets instanciés
print(ma_voiture.marque)
print(ma_voiture.modele)

print(ta_voiture.marque)
print(ta_voiture.modele)

print(voiture_Daniel.marque)
print(voiture_Daniel.modele)

ma_voiture.marque = "Toyota"
ma_voiture.modele = "Yaris"

# Méthodes
ma_voiture.afficher_informations()
ta_voiture.afficher_informations()
voiture_Daniel.afficher_informations()