# RETO 41

#  Enunciado: Crea una función que calcule el valor del parámetro perdido
#  correspondiente a la ley de Ohm.
#  Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
#  el valor del tercero (redondeado a 2 decimales).
#  - Si los parámetros son incorrectos o insuficientes, la función retornará
#  la cadena de texto "Invalid values".
#  

# Useful formulas:
# V = Voltage, I = Current, R = Resistance
# V = I * R
# I = V / R
# R = V / I

def main() -> None:
    print(calc_ohm(4, None, 2))


def calc_ohm(v: int, r: int, i: int) -> str:
    """
        Calculate the resulting number either voltage, resistance or current based
        on what parameters were given

        Parameters
        v: Voltage
        r: Resistance
        i: Current

        Return
        String containing the result of the calculation
    """
    result: str

    if not v and (i and r):
        result = f"Voltage = {i * r:.2f}"
    elif not r and (v and i):
        result = f"Resistance = {v / i:.2f}"
    elif not i and (v and r):
        result = f"Current: {v / r:.2f}"
    else:
        return "Oops, not enough params"

    return result


if __name__ == '__main__':
    main()