#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

listaDeAsignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
salvadas = []

for asignatura in listaDeAsignaturas:
    nota = int(input("Ingrese la nota para " + asignatura))
    if (nota >= 5):
     salvadas.append(asignatura)

for asignatura in salvadas:
    listaDeAsignaturas.remove(asignatura)

print(listaDeAsignaturas)
    