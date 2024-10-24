#promedio duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5 

#diferencias de duracion 

diferencias_con_min = diferencias_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_con_max = 100 - dalto_curso *1000 // otros_cursos_max /10
diferencias_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_vacio_dalto = 100 - dalto_curso *1000 // crudo_dalto /10

#mostrando la diferencia de tiempo de duracion (ejercicio a)
print("----------------")
print(f"El curso de Dalto dura un {diferencias_con_min}% menos que el mas rápido")
print(f"El curso de Dalto dura un {diferencias_con_max}% menos que el mas lento")
print(f"El curso de Dalto dura un {diferencias_con_promedio}% menos que el promedio de los curos")

#mostrando diferencia de crudo (ejercicio b)
print("----------------")
print(f" Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f" El curso de Dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio")

#mostrar diferencias si los cursos duraran diez horas
print("----------------")
print(f"Ver diez horas de este curso equivale a ver {otros_cursos_promedio *1000 // dalto_curso /100} horas de otros cursos")
print(f"Ver diez horas de otros cursos equivale a ver {dalto_curso *1000 // otros_cursos_promedio /100} horas del curso dalto")
print("----------------")