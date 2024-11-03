#
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
#
import os

CONTRASEÑA = "AbMo"

def pide_contraseña():
    contraseña = ""
    while contraseña != CONTRASEÑA:
        contraseña = input("Escribe la contraseña correcta: ")
        os.system("cls")
        if contraseña == CONTRASEÑA:
            print("Enhorabuena!!!, es la contraseña correcta.")
        else:
            print("Te has equivocado, esa no es la contraseña.")


def main():
    pide_contraseña()


if __name__ == "__main__":
    main()