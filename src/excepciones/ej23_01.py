#
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
#

def años_cumplidos(edad):
    for i in range(1, edad+1):
        print(i)

def main():
    edad = input("Ingrese la edad: ")

    try:
        edad = int(edad)
        if edad <= 0:
            raise NameError
        else:
            años_cumplidos(edad)
    except ValueError:
        print("Lo que has introducido no es un número.")
    except NameError:
        print("El número debe ser mayor que 0")

if __name__ == "__main__":
    main()