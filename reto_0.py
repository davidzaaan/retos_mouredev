"""
  Escribe un programa que muestre por consola (con un print) los
  números de 1 a 100 (ambos incluidos y con un salto de línea entre
  cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def main() -> None:
    for num in range(1, 101):
        fizzbuzz(num)


def fizzbuzz(number: int) -> str:
    """
        Function that determinates if the given number matches with the fizz buzz game requirements

        Params
            number[int] -> The number to determinate if is a fizz, buzz or both
        
        Return
            str -> ["fizz", "buzz", "fizzbuzz]
    """
    FIZZ = "fizz"
    BUZZ = "buzz"
    FIZZBUZZ = "fizzbuzz"

    if (number % 3 == 0) and (number % 5 == 0):
        print(FIZZBUZZ)
    elif number % 3 == 0:
        print(FIZZ)
    elif number % 5 == 0:
        print(BUZZ)


if __name__ == '__main__':
    main()