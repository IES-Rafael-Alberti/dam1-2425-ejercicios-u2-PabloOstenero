#
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática 
# el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y 
# mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ 
# y si es mayor de 18 años, 10€.
#

def pide_edad():
    edad = int(input("Dime tu edad: "))
    return edad

def mostrar_precio(edad):
    if edad < 4:
        print("Puede entrar gratis!!!")
    elif edad < 18:
        print("Tiene que pagar 5€")
    else:
        print("Tiene que pagar 10€")

def main():
    edad = pide_edad()

    mostrar_precio(edad)

if __name__ == "__main__":
    main()