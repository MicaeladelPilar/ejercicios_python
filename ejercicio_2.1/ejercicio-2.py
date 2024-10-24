#crear una funcion que devuelva los numeros primos entre 0 y el numero ingresado por el usuario 

#crear funcion que verifique si el numero es primo 
def es_primo(num):
    #se verifica que el numero pasado no pueda dividirse por ningun numero entre dos y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno se retorna false y termina el bucle
        if num%i==0: return False
        #si termina el bucle significa que es primo
    return True

#creando una funcion que retorne una lista con los numeros primos
def primos_hasta (num):
    #se crea la lista
    primos = []
    for i in range (3,num+1):
        #se verifica si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea se lo agrega a la lista
        if resultado== True: primos.append(i)
        #se devuelve la lista
    return primos
#se muestra el resultado
resultado = primos_hasta(98)
print(resultado)

