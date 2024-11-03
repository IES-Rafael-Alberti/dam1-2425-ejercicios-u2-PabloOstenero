#
# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
# Deberá solicitar el número hasta introducir uno correcto.
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
    try:
        num = int(input("Ingrese un numero: "))
        if num < 1:
            raise NameError
        mostrar_cuenta_atras(num)
    except ValueError:
        print("Tienes que escribir un número.")
    except NameError:
        print("El número tiene que ser positivo")


if __name__ == "__main__":
    main()