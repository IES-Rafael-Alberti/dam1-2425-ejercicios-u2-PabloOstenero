#
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
# así como la cantidad de dinero que recibirá el usuario.
#

def pide_puntuacion():
    return float(input("Escribe tu puntuacion: "))

def calcula_nivel_y_dinero(punt):
    if punt == 0.0:
        print(f"El nivel de su rendimiento es Inaceptable y recibirá {2400 * punt}€.")
    elif punt == 0.4:
        print(f"El nivel de su rendimiento es Aceptable y recibirá {2400 * punt}€.")
    elif punt >= 0.6:
        print(f"El nivel de su rendimiento es Meritorio y recibirá {2400 * punt}€.")
    else:
        print("No es posible tener ese nivel de rendimiento")

def main():
    puntuacion = pide_puntuacion()

    calcula_nivel_y_dinero(puntuacion)


if __name__ == "__main__":
    main()