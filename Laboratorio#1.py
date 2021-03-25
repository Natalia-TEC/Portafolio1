#Laboratorio 1

#Ejercicio1
""" Hacer una función llamado que calcule el área de un trapecio
Nombre: areaTrapecio
Entradas: (B) la base mayor, (b) la base menor y (a) la altura
Salida: el resultado del área del trapecio
Restrucciones: las entradas tienen que ser números positivos, y (b, a) tienen que ser menor a B
"""

def areaTrapecio(B, b, h):
    if((B >= 0)and (b >= 0)and (B > b)and (h >= 0)and (B > h)):
        area = ((B + b) * h)/2 #Fórmula del área de un Trapecio
        return area
    else:
        return print("Error: uno de los parámetros no cumple con las restricciones de ser un número positivo o que los parámetros (b, h) sean menor que el parámetro B, vuelva a intentarlo.")

#Ejercicio2
""" Implemente una función llamada grupoPoblacion(edad), que retorne el grupo de la población a la que pertenece según su edad.
Nombre: grupoPoblacion
Entrada: (edad) cantidad de años que posee la persona
Salida: resultado del grupo de la población a la que pertenece
Restricciones: tiene que ser un número entero positivo que este dentro del rango de 0 a 125
"""

def grupoPoblacion(edad):
    if(isinstance(edad, int)and (edad >=0 )and (edad <= 125)):#restricciones
        if((edad >= 0)and (edad <= 10)):#Categorias
            return print("El grupo al que pertence es: Niños")
        elif((edad > 10)and (edad <= 18)):
            return print("El grupo al que pertence es: Adolecentes")
        elif((edad > 18)and (edad <= 50)):
            return print("El grupo al que pertence es: Adultos")
        elif((edad > 50)and(edad <= 125)):
            return print("El grupo al que pertence es: Ancianos")
        else:
            return print("Error")
    else:#Parámetros no incluidos
        if(not (edad >= 0)):
            print("El valor no se encuentra dentro del rango de 0 a 125, vuelva a intentarlo.")
        if(not (edad <= 125)):
            print("Es una edad poco probable, favor consultar")
                       
#Ejercicio3
""" Implemente una función llamada sonImpares(num)
Nombre: sonImpares(num)
Entrada: (num)un número entero positivo mayor a cero
Salidas: (True) si todos los digitos del num son impares y (False) si uno o más dígitos de num no son impares.
Restricciones:num tienen que ser un número entero positivo mayor que cero y que todos los dígitos sean impares para retornar un (True)
"""

def sonImpares(num):
    if(isinstance(num, int)== False):
        return print("Error, el parámetro de entrada debe de ser un número entero.")
    if(num < 10):
        if(num % 2 == 0):
            return False
        else:
            return True
    else:
        if((num % 10) % 2 == 0):
            return False and sonImpares(num // 10)
        else:
            return True and sonImpares(num // 10)

    

#Ejercicio4
        
"""Implemente una función llamada construirNumero(num, divisor)
Nombre: construirNumero
Función:El objetivo de este es dividir cada dígito de num de derecha a izquierda, y utilizar el resultado de la división entera para construir el nuevo número.
Entrada: (num, divisor) números enteros positivos mayor que cero.
Salidas: El nuevo número.
Restricciones: (num) número entero positivo mayor que cero, (divisor) tiene que ser un número mayor que cero y menor que 10."""

def construirNumero(num, divisor):
    if(isinstance(num, int)and (num > 0)and isinstance(divisor, int)and (divisor > 0)and (divisor <10)):
        return construirNumero_aux(num, divisor, 0)
    else:
        return print("Error: los parámetros no son validos, vuelva a intentarlo.")

def construirNumero_aux(num, divisor, indice):
    if(num == 0):
        return 0
    else:
        return (num % 10)//divisor  * 10 ** indice + construirNumero_aux(num // 10, divisor, indice +1)
