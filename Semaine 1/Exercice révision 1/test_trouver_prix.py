import pytest
import trouver_prix

@pytest.mark.parametrize("produit, prix", [
    ("Oranges", 2.99),
    ("Pommes", 3.45),
    ("Bananes", 0.99),
    ("Aubergines", 3.45),
    ("Pommes de terre", 5.99),
    ("Lait", -1),
    ("Pain", -1)
])
def test_trouver_prix(produit, prix):
    assert trouver_prix.trouver_prix(produit) == prix