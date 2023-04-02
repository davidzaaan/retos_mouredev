"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
import time
fib_cache = {}

def main() -> None:
    start = time.perf_counter()
    print(fibonacci(50))
    end = time.perf_counter()

    print(f"Total time elapsed: {end - start}s")
    

def fibonacci(number: int) -> list:
    """
        Function that calculates the fibonacci series starting from 0
    """
    fibonacci_series: list = []

    start, end = 0, 1
    next = start + end

    for num in range(number):
        if num == 0:
            fibonacci_series.append(start)
            fibonacci_series.append(end)

        fibonacci_series.append(next)

        start = end
        end = next
        next = start + end

    return fibonacci_series


if __name__ == '__main__':
    main()