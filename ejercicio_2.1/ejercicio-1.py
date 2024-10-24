#falto el profesor a clase y los alumnos preparan la clase 

#pedir el nombre y la edad de los alumnos que fueron a clase

def obtener_compañeros(cantidad_de_compañeros) :
    compañeros =  []
    for i in range (cantidad_de_compañeros):
        nombre = input("Ingresar el nombre del compañero: ")
        edad= int(input("Ingresar la edad del compañero: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key= lambda X:X [1]) #ordena (la funcion sort() ordena) los compañeros por la key (el segundo valor de la tupla)
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente,profesor = obtener_compañeros (5)

print(f"El profesor es : {profesor} y su asistente es {asistente }")