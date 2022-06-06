"""
#Condicional IF

Si se_cumple_esta_condicion:
    Ejercutar grupo de instrucciones
Si No:
    se ejecutan otro grupo de instrucciones

if condicion:
    Instrucciones
else:
    otras intrucciones   

# Operadores de comparacion:
== <-- Significa igual
!= <-- Diferente
<  <-- menor que
>  <-- mayor que 
<= <--menor o igual que
>= <-- mayor igual que 
"""

# Ejemplo 1
print("\n############## EJEMPLO 1 #################")

color = "rojo"

if color == "rojo":
    print("Si es el color rojo")
else:
    print("Este color no es el color rojo")    


#Ejemplo2
print("############## EJEMPLO 2 #################")

year = int(input("En que año estamos?: "))

if year >= 2021:
    print("Estamos en 2021 en adelante !!")
else:
    print("Es un año anterior a 2021")

