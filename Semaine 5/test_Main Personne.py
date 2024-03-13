import pytest
from Personne import Personne
def test_age_valide():
    personne = Personne(age=20)
    assert personne.age == 20

def test_age_invalide():
    with pytest.raises(ValueError):
        personne = Personne(age=-5)

@pytest.mark.parametrize("age, age_attendu", [(30, "Félicitations! Vous avez 31 ans!"),(25, "Félicitations! "
"Vous avez 26  ans!")])
def test_feter_anniversaire(age, age_attendu):
    personne = Personne(age=age)
    assert personne.feter_anniversaire() == age_attendu
