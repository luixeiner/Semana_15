from io import open_code


print = ("Bienbenidos al menu")
print = ("+"*40)

opcion = input("leer o escribir (L/E)")
if opcion == "E":
    texto = input("Escribe una frase: ")
    file = open ("archivo2.txt" , "w")
    file.write ("texto: " + texto )
else:
    file = open ("archivo2.txt" , "r")
    print (file.read())
    
