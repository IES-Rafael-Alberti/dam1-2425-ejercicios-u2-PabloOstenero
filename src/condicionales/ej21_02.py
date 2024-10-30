#
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario 
# coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
#

def comprobar_contraseña(contraseña, prueba):
    if contraseña.lower() == prueba.lower():
        print("Congratulations!! has puesto la contraseña correcta")
    else:
        print("Ooooh, te has equivocado al ponerlo la segunda vez")

def main():

    contraseña = input("Introduce la contraseña: ")
    prueba_contraseña = input("Repite la contraseña: ")

    comprobar_contraseña(contraseña, prueba_contraseña)



if __name__ == "__main__":
    main()