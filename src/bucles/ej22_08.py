#
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#

def mostrar_triangulo(num):
    cadena = ""
    for i in range(1, num+1, 2):
        for n in range(i, 0, -2):
            cadena += str(n) + " "    
        print(cadena)
        cadena = ""


def main():
    num = int(input("Dame un número entero para hacer el triángulo: "))

    mostrar_triangulo(num)


if __name__ == "__main__":
    main()