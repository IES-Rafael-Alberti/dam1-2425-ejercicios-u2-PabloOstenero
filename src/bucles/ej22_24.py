#
# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
#

def primo(numero):
    primo = True
    for i in range(2, int(numero/2)+1):
        if numero % i == 0:
            primo = False

    return primo

def primos_ingresados():
    numero = -1
    num_primo = 0

    while numero != 0:
        numero = int(input("Escribe un número mayor que 1 o 0 para salir: \n"))
        if numero < 0:
            print("El número tiene que ser positivo")
        elif numero == 0:
            print("Bye bye")
        else:
            if primo(numero):
                num_primo += 1

    print(f"Has ingresado {num_primo} números primos.")

def main():
    primos_ingresados()


if __name__ == "__main__":
    main()