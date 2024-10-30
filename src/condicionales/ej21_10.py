#
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
#

def elige_topping(veg):
    if veg == "s":
        topping = input("Estos son los ingredientes para una pizza vegetariana: \n Pimiento \n Tofu \nElige uno: \n").lower()
        if topping == "pimiento" or topping == "tofu":
            return topping
        else:
            return None
    elif veg == "n":
        topping = input("Estos son los ingredientes para una pizza no vegetariana: \n Peperoni \n Jamón \n Salmón \nElige uno: \n").lower()
        if topping == "peperoni" or topping == "jamón" or topping == "salmón":
            return topping
        else:
            return None
    else:
        print("No entiendo que quiere.")
        return None

def mostrar_pizza(veg, topping):
    if topping == None:
        print("Ha ocurrido un error al elegir un topping.")
    else:
        if veg == "s":
            print(f"La pizza es vegetariana y sus ingredientes son: \n Mozzarella \n Tomate \n {topping.capitalize()}")
        elif veg == "n":
            print(f"La pizza no es vegetariana y sus ingredientes son: \n Mozzarella \n Tomate \n {topping.capitalize()}")


def main():
    veg = input("¿Quieres una pizza vegetariana? s/n \n").lower()
    
    topping = elige_topping(veg)

    mostrar_pizza(veg, topping)

if __name__ == "__main__":
    main()