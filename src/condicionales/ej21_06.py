#
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N 
# y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y 
# muestre por pantalla el grupo que le corresponde.
#

def pedir_nombre():
    nombre = input("Escribe tu nombre: ").lower()
    return nombre

def pedir_sexo():
    sexo = input("Escribe tu sexo: ").lower()
    return sexo

def mostrar_grupo(nombre, sexo):
    if (sexo[0] == "h" and nombre[0] >= "n") or (sexo[0] == "m" and nombre[0] < "m"):
        print("Forma parte del grupo A.")
    else:
        print("Forma parte del grupo B.")

def main():
    nombre = pedir_nombre()
    sexo = pedir_sexo()

    mostrar_grupo(nombre, sexo)

if __name__ == "__main__":
    main()