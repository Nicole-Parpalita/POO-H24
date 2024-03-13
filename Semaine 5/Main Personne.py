from Personne import Personne


personne1 = Personne("123456789", "Nicole", 18)
dict_personnes[personne1.num_ass_soc] = personne1.nom, personne1.age
personne2 = Personne("000000000", "Jojo", 30)

print(Personne.dict_personnes)
print(Personne.feter_anniversaire(personne1))
print(Personne.est_majeur(personne1.age))
Personne.trouver_personnes_majeures()
Personne.trouver_personnes_majeures2()