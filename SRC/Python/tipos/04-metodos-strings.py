animal = "  chanCHito feliz   "
print(animal)
print(animal.upper())  # agrega todo a mayusculas//
print(animal.lower())  # agrega todo a minusculas
print(animal.capitalize())  # el 1° caracter sera Mayuscula
# se puede agregar delante del capitalize para que en el TERMINAL se pueda ver
print(animal.strip().capitalize())
print(animal.title())  # Agrega Mayusculas en cada nueva palabra
print(animal.strip())  # Elimina todos los (espacios) al inicio y al final
print(animal.lstrip())  # Elimina los (espacios) a la izquierda
print(animal.rstrip())  # Elimina los (espcios) a la derecha
# Nos indica en que posición esta este string, es un INDICE
print(animal.find("CH"))
# Cuando agregamos algo que no existe en la variable, nos arroja en el terminal -1
print(animal.find("cH"))
# No funciono debido a que el string no esta bien escrito
print(animal.replace("nch", "j"))
print(animal.replace("nCH", "j"))  # Esto sí da "  chajito feliz   "
# Busca si la cadena de caracteres se encuentra dentro del string y lo hace con un Boolean
print("nCH" in animal)
# Busca si la cadena de caracteres no se encuentra y tambien es un Boolean
print("nCH" not in animal)
