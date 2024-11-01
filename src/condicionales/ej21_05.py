#
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario 
# tiene que tributar o no.
#


def pedir_edad():
    try:
        edad = int(input("Dime tu edad: "))
        return edad
    except ValueError:
        print("Tu edad debe ser un número.")
        return -1

def pedir_ingreso():
    try:
        ingreso = int(input("Dime tus ingresos mensuales: "))
        return ingreso
    except ValueError:
        print("Tu edad debe ser un número.")
        return -1

def tributa(edad, ingreso):
    if edad == -1 or ingreso == -1:
        return "Ha ocurrido un error."
    elif edad < 16 or ingreso < 1000:
        return "No tributa."
    else:
         return "Tributa"

def main():
    edad = pedir_edad()
    ingreso = pedir_ingreso()

    trib = tributa(edad, ingreso)

    print(trib)


if __name__ == "__main__":
    main()