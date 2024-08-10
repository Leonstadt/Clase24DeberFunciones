x = 10 # Variable global
def mi_funcion():
    #x = 5 # Variable local
    print(f"Variable local x dentro de la función: {x}")
mi_funcion()
print(f"Variable global x fuera de la función: {x}")