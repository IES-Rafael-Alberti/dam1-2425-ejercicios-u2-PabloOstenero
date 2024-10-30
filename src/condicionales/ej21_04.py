#
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
#

def par_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def mostrar_pantalla(par):
    if par == True:
        print("El número es par")
    else:
        print("El número es impar")


def main():
    num = int(input("Escribe un número: "))

    par = par_impar(num)

    mostrar_pantalla(par)



if __name__ == "__main__":
    main()