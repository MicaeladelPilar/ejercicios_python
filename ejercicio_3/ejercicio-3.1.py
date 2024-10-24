import re 

#detectando un nuemro de CABA y ocultandolo

texto = "Hola, mi numero de telefono celular es: +54 11 4444-5555"

pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

remplazo = re.sub(pattern,"(Número oculto)",texto)

print(remplazo)