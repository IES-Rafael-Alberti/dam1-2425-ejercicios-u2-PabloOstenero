#
# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
#

def mostrar_impares(num):
    cadena = ""
    for i in range(1, num+1, 2):
        if i == num or i == num-1:
            cadena += str(i)
        else:
            cadena += str(i) + ", "

    print(cadena)

def main():
    try:
        num = int(input("Ingrese un numero: "))
        if num < 1:
            raise NameError
        mostrar_impares(num)
    except ValueError:
        print("Tienes que escribir un número.")
    except NameError:
        print("El número tiene que ser positivo")


if __name__ == "__main__":
    main()