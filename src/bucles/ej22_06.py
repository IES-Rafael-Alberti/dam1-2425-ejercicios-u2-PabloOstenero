#
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido.
#

def mostrar_triangulo(num):
    for i in range(1, num+1):
        print("*" * i)


def main():
    num = int(input("Dime la altura del triángulo: "))

    mostrar_triangulo(num)


if __name__ == "__main__":
    main()