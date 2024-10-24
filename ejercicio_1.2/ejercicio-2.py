frase = input("Introducí una frase y te calculo cuanto tiempo tardarias si tuvieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print("--------------------")
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print("--------------------")
print(f"Una persona que habla un 30% mas  lo diria en {cantidad_de_palabras} palabras, y tardaria    {(cantidad_de_palabras/ 2) / 1.3} segundos en decirlo")
if cantidad_de_palabras >120:
    print("Estas hablando mucho")