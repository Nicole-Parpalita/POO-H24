import offrir_fruit
import pytest

@pytest.mark.parametrize("nom_de_famille_initial, nom_de_famille_verifie", [
    ("Parpalita", "Parpalita"),
    ("Jo=Seph", None),
    ("Po", None),
    ("Lores", "Lores")
])
def test_verifier_nom_de_famille(nom_de_famille_initial, nom_de_famille_verifie):
    assert offrir_fruit.verifier_nom_de_famille(nom_de_famille_initial) == nom_de_famille_verifie
