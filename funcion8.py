def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
numero=int(input("Ingrese el numero a calcular el factorial: "))
print(f"El factorial del numero es: {factorial(numero)}")