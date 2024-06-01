#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

ganadores = []
for i in range(6):
    numero = input("Ingrese un numero")
    ganadores.append(numero)
    ganadores.sort()

print("los numeros ganadores son :"+ str(ganadores))


    
   
        
