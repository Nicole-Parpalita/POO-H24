prix_fruits = {"Oranges": 2.99, "Pommes": 3.45, "Bananes": 0.99, "Bleuets":2.99}

prix_legumes = { "Carottes": 2.99, "Aubergines": 3.45, "Pommes de terre": 5.99, "Épinards": 1.99}


def trouver_prix(produit: str) -> float:
    """
    Trouver et retourner le prix d'un produit
    :param produit: Le produit
    :return: Le prix du produit ou -1 si le produit est inexistant
    """
    if produit in list(prix_fruits.keys()):
        return prix_fruits[produit]
    elif produit in list(prix_legumes.keys()):
        return prix_legumes[produit]
    else:
        return -1


if __name__ == "__main__":
    produit = input("Entrez un produit: ").strip().capitalize()
    print(trouver_prix(produit))



