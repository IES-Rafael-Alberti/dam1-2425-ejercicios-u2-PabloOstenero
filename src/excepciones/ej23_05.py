#
# Escribir que solicite una contraseña, y si no coincide con la que se tiene, 
# lance la excepción NameError con el mensaje, "Incorrect Password!!"
#

CONTRASEÑA = "AbCDe"

def comprueba_contraseña(intento):
    try:
        if intento != CONTRASEÑA:
            raise NameError
        print("Correct!!")
    except NameError:
        print("Incorrect Password!!")

def main():
    intento = input("Escribe la contraseña: \n")

    comprueba_contraseña(intento)

if __name__ == "__main__":
    main()