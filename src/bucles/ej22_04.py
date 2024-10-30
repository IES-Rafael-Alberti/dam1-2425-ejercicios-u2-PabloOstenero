#
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero
# separados por comas.
#

def mostrar_cuenta_atras(num):
    cadena = ""
    for i in range(num, -1, -1):
        if i == 0:
            cadena += str(i)
        else:
            cadena += str(i) + ", "

    print(cadena)

def main():
    num = -1
    while(num < 1):
        num = int(input("Ingrese un numero: "))
        if num < 1:
            print("El número tiene que ser positivo")

    mostrar_cuenta_atras(num)


if __name__ == "__main__":
    main()