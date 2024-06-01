
#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> 
# has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista 
# y <nota> cada una de las correspondientes notas introducidas por el usuario.


listaDeAsignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Informatica"]
notas = []

for asignatura in listaDeAsignaturas:   
    nota = input("¿Qué nota has sacado en " + asignatura + "?")
    notas.append(nota)

for i in range(len(listaDeAsignaturas)):
    print("En " + listaDeAsignaturas[i] + " has sacado " + notas[i])
    