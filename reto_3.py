"""
 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
"""

def main() -> None:
    prime_numbers: list = []

    for number in range(2, 101):
        if is_prime(number):
            prime_numbers.append(number)

    print(prime_numbers)


def is_prime(number: int) -> bool:
    """
        Function that determines if a given number is prime

        Params
            number[int] The number to be checked
        
        Returns
            is_prime[bool] Boolean variable the states if the number was or not prime
    """
    i = 2
    is_prime: bool = True

    while True:
        # Applies only if the number given is 2
        if i == number:
            break
        # Assuming that any prime number is only divisble by one and by itself...
        # ...then if it found at least one more divisor, breaks the loop
        if (number % i == 0):
            is_prime = False
            break

        i += 1
    
    return is_prime


if __name__ == '__main__':
    main()