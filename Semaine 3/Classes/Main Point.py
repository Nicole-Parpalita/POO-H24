from Point import Point
import math

point1 = Point(2, 3)
point2 = Point(2, 4)

def calculer_distance(p_point1: Point, p_point2: Point) -> float:
    """
    Calcule la distance entre point 1 et point2
    :param point1: Le point 1
    :param point2: Le point 2
    :return: La distance entre les deux points
    """
    distance = math.sqrt((p_point2.x - p_point1.x) ** 2 + (p_point2.y - p_point1.y) ** 2)
    return distance


distance = calculer_distance(point1, point2)


point1.afficher_informations()
point2.afficher_informations()
print(f"La distance entre le point 1 et le point 2 est de {distance}")
