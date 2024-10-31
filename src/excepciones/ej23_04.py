#
# Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, 
# mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
#

def numero_entero(numero):
    try:
        numero = int(numero)
        print(f"El número introducido es {numero}")
    except ValueError:
        print("La entrada no es correcta")

def main():
    numero = input("Escribe un número entero: ")

    numero_entero(numero)

if __name__ == "__main__":
    main()