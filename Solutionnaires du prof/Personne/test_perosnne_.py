import pytest
from Classe_Personne import Personne


@pytest.mark.parametrize("age,age_attendu", [
    (12, 12),
    (0, 0),
    (130, 130),
    (131, 0),
    (60, 60),
    (1, 1),
    ("4444782", 0),
    ("Christophe", 0),
    ("$?",  0),
    ("12$$ddddd", 0),
    ("1", 0),
    ("3455555608483282828282", 0),
    (12.5,  0),
    (-5.5, 0),
    (0.0, 0),
    (130.0, 0),
    (131.5, 0)
])
def test_propriete_age(age,  age_attendu):
    """
    Permet de tester la propriété age
    :param age: l'âge utilisé pour initialiser la propriété age
    :param age_attendu: La valeur attendue de
                        la propriété age après son initialisation
    :return: None
    """
    # Arrange
    une_personne = Personne()
    # Act
    une_personne.age = age
    # Assert
    assert une_personne.age == age_attendu
