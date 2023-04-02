# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */
from math import pi, tan

def main() -> None:
    print(area("triangle"))
    print(area("square"))
    print(area("rectangle"))
    print(area("dog"))


def area(polygon: str) -> str:
    """
        Function that calculates the area of a polygon

        Params
            poligon[str] The polygon to calculate the area
        
        Returns
            area[int] The area of the polygon calculated
    """
    SQUARE: str = "square"
    TRIANGLE: str = "triangle"
    RECTANGLE: str = "rectangle"

    valid_polygons = [SQUARE, TRIANGLE, RECTANGLE]

    if not polygon.lower() in valid_polygons:
        return f"Polygon '{polygon}' not supported\nSupported polygons are [Triangle, Square, Rectangle]"
    
    sides: int
    side: int = 5

    if (polygon == SQUARE) or (polygon == RECTANGLE):
        sides = 4
    elif polygon == TRIANGLE:
        sides = 3

    # With this it will find the apothem
    apothem: float = (1 / 2) * side * (1 / tan(pi / sides))

    area: float = (1 / 2) * sides * apothem * side

    return f"The Area of a '{polygon}' is: {area}"


if __name__ == '__main__':
    main()