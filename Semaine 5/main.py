from Classe_Vetement import Vetement

vetement1 = Vetement()
vetement1.type = "Sport"
vetement1.prix = 15
vetement1.larg = 80
vetement1.long = 150.5
print(vetement1.type)
vetement2 = Vetement()
vetement2.type = "Occasion"
vetement2.prix = 50
print(vetement1 + vetement2)
print(len(vetement1))
print(Vetement.tissu)
print(vetement1.tissu)
vetement3 = Vetement()
print(Vetement.nb_vetements)
print(Vetement.verifier_nb_instances(5))
print(Vetement.afficher_vetements())
print(Vetement.somme(80.5, 99.5))