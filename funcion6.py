def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion
re_suma, re_resta,re_multiplicacion = operaciones_basicas(8, 3)
print(f"Suma: {re_suma}, Resta: {re_resta}, Multiplicacion: {re_multiplicacion}")