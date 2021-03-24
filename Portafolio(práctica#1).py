#Portafolio(Practica #1)

#Multiplicación de forma recursiva.

"""
Nombre: multiplicarRecusivo(num, factor)
Entradas:(num) número que queremos multiplicar, (factor) número que multiplica.
Salidas: resultado de la multiplicación de forma recursiva.
Restricciones: debe de ingresar números enteros positivos.
Objetovo: multiplicar un número n por un número m sin utilizar el operador de multiplicación.
"""

def multiplicarRecusivo(num, factor):
    if(isinstance(num, int)and (num>=0)and isinstance(factor, int)and (factor>=0)):
        return multiplicarRecusivo_aux(num, factor)
    else:
        return print("Error:los parámetros de entrada no cumplen con la restricción de ser un número entero positivo, vuelva a intentarlo.")

def multiplicarRecusivo_aux(num, factor):
    if(factor == 0):
        return 0
    else:
        return num + multiplicarRecusivo_aux(num, factor-1)
    
#División de forma recursiva.

"""
Nombre: divisionRecusivo(divisor, dividendo)
Entradas:(divisor) número que queremos dividir, (dividendo) cantidad de veces que queremos dividir al divisor.
Salidas: resultado de la división de forma recursiva.
Restricciones: debe de ingresar números enteros positivos.
Objetivo: Dar el reusltado de la división entera de un número n por un número m sin utilizar el operador de la división.
"""

def divisionRecusivo(divisor, dividendo):
    if(isinstance(divisor, int)and (divisor>=0)and isinstance(dividendo, int)and (dividendo>=0)):
        return divisionRecusivo_aux(divisor, dividendo)
    else:
        return print("Error: los parámetros de entrada no cumplen con la restricción, vuelva a intentarlo de nuevo.")

def divisionRecusivo_aux(divisor, dividendo):
    if(divisor - dividendo < 0):
        return 0
    else:
        return 1 + divisionRecusivo_aux(divisor - dividendo, dividendo)



    
