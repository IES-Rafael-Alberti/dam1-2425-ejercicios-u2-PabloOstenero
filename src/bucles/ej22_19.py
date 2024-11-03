#
# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
# El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
# Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú 
# y el programa finalizará.
#
import os
import time

def menu():
    opcion = 0
    while opcion != 3:
        opcion = int(input("Escibe una de estas opciones: \n 1- comenzar programa \n 2- imprimir listado \n 3-finalizar programa \n"))
        if opcion == 1 or opcion == 2:
            print(f"Has elegido la opción {opcion}")
            time.sleep(5)
            os.system("cls")
        elif opcion == 3:
            time.sleep(5)
            os.system("cls")
        else:
            print("Esta opción no existe.")
            time.sleep(5)
            os.system("cls")



def main():
    menu()


if __name__ == "__main__":
    main()