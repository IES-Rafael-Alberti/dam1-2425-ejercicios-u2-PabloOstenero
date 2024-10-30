#
# Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
# finalizando el ingreso al leerse el string “*” (asterisco). 
# Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. 
# Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total 
# (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
#

def titulos_libros():
    titulo = ""
    digitos = 0
    salto = 0
    while titulo != "*":
        titulo = input("Libro: ")
        if titulo == "/":
            salto += 1
            print(f"Línea completa. Aparecen {digitos} dígitos numéricos.")
            digitos = 0
        else:
            for i in range(len(titulo)):
                if titulo[i].isdigit():
                    digitos += 1
    
    print(f"Se leyeron {salto} líneas completas.")


def main():
    titulos_libros()

if __name__ =="__main__":
    main()