#y = 10
variable=20
def modificar_global():
    #global y
    #y = 20
    global variable
    variable=40
    print(f"Variable global y modificada dentro de la función: {variable}")
modificar_global()
print(f"Variable global y fuera de la función: {variable}")