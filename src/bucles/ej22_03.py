#
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares
# desde 1 hasta ese número separados por comas.
#

def mostrar_impares(num):
    cadena = ""
    for i in range(1, num+1, 2):
        if i == num or i == num-1:
            cadena += str(i)
        else:
            cadena += str(i) + ", "

    return cadena

def main():
    num = -1
    while(num < 1):
        num = int(input("Ingrese un numero: "))
        if num < 1:
            print("El número tiene que ser positivo")

    cadena = mostrar_impares(num)

    print(cadena)


if __name__ == "__main__":
    main()