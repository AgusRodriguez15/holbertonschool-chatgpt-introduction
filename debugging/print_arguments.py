#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: {} <número>".format(sys.argv[0]), end="")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            print("El número debe ser no negativo.")
        else:
            print("Factorial de {}: {}".format(num, factorial(num)), end="")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")