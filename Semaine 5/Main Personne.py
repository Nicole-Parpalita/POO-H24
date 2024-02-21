from Personne import Personne

dict_personnes = {}

personne1 = Personne("123456789", "Nicole", 18)
dict_personnes[personne1.num_ass_soc] = personne1.nom, personne1.age
personne2 = Personne("000000000", "Jojo", 30)
dict_personnes[personne2.num_ass_soc] = personne2.nom, personne2.age

print(Personne.feter_anniversaire(personne1))
print(Personne.est_majeur(personne1.age))
print(Personne.trouver_personnes_majeures())