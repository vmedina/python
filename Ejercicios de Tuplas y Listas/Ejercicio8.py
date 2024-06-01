#Ejercicio 9
#Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Ingrese una palabra")
vocales = "aeiouAEIOU"
indiceA = 0
indiceE = 0
indiceI = 0
indiceO = 0 
indiceU = 0
indice = 0
for letra in palabra:
    if letra in vocales:
        indice+=1
    if letra == "A" or letra == "a":
        indiceA +=1
    if letra == "E" or letra == "e":
        indiceE +=1
    if letra == "I" or letra == "i":
        indiceI +=1
    if letra == "O" or letra == "o":
        indiceO +=1
    if letra == "U" or letra == "u":
        indiceU +=1
        
print (indice)
print("Cantidad de A " + str(indiceA))
print("Cantidad de E " + str(indiceE))
print("Cantidad de I " + str(indiceI))
print("Cantidad de O " + str(indiceO))
print("Cantidad de U " + str(indiceU))