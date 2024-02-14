from Rectangle import Rectangle

rectangle1 = Rectangle(2, 4)
rectangle2 = Rectangle(3, 5)

def calculer_périmètre(rectangle: Rectangle) -> float:
    """
    Calculer le périmètre d'un rectangle
    :param rectangle: Les mesures du rectangles
    :return: Le périmètre du rectangle
    """
    perimetre = 2 * rectangle.longueur + 2 * rectangle.largeur
    return perimetre

def calculer_aire(rectangle: Rectangle) -> float:
    """
    Calculer l'aire d'un rectangle
    :param rectangle: Les mesures du rectangles
    :return: L'aire du rectangle
    """
    aire = rectangle.longueur * rectangle.largeur
    return aire

def est_carre(rectangle: Rectangle) -> bool:
    """
    Vérifie si le rectangle est carré
    :param rectangle: Les mesures du rectangles
    :return: True s'il est carré, False si non
    """
    if rectangle.longueur == rectangle.largeur:
        return True
    else:
        return False

def afficher_rectangle(longueur: float, largeur: float, perimetre: float, aire: float, carre: bool) -> str:
    """
    Affiche toutes les informations relatives au rectangle.
    :param longueur: La longueur du rectangle
    :param largeur: La largeur du rectangle
    :param perimetre: Le périmètre du rectangle
    :param aire: L'aire du rectangle
    :param carre: Si le rectangle est carré ou nom
    :return: Les informations
    """
    print(f"""\n
La longueur du rectangle est de {longueur}.
La largeur du rectangle est de {largeur}.
Le perimetre du rectangle est de {perimetre}.
L'aire du rectangle est de {aire}.
{carre}""")


# Main
# Rectangle 1
perimetre1 = calculer_périmètre(rectangle1)
aire1 = calculer_aire(rectangle1)
carre1 = est_carre(rectangle1)
if carre1 == False:
    carre1 = "Il ne s'agit pas d'un carré."
else:
    carre1 = "Il s'agit d'un carré."
afficher_rectangle(rectangle1.longueur, rectangle1.largeur, perimetre1, aire1, carre1)

# Rectangle 2
perimetre2 = calculer_périmètre(rectangle2)
aire2 = calculer_aire(rectangle2)
carre2 = est_carre(rectangle2)
if carre2 == False:
    carre2 = "Il ne s'agit pas d'un carré."
else:
    carre2 = "Il s'agit d'un carré."
afficher_rectangle(rectangle2.longueur, rectangle2.largeur, perimetre2, aire2, carre2)