#Super primo.

"""
Nombre: superPrimo(num)
Entradas: que reciba como entrada un número entero positivo denominado (num)
Salidas: que retorne si cumple (True) o no los requisitos (False) de número súper primo. 
Restricciones: Debe de recibir un número entero positivo diferente de cero como parámetro de entrada-
"""

def superPrimo(num):
    if(isinstance(num, int)and (num > 0)):
        return (superPrimo_aux(num, 0))
    else:
        return print("Error en la entrada.")

def superPrimo_aux(num, suma):
    if(num==0):
        return primo(suma)
    digito = num % 10
    if(digito % 2 == 1):
        suma += digito
    return superPrimo_aux(num // 10, suma)


#--------------------------------------
def primo(num):
    if(num >= 2):
        return primo_aux(num, num//2)
    return False

def primo_aux(num, div):
    if(div == 1):#div significa divisor
        return True
    if(num % div == 0):
        return False
    return primo_aux(num, div - 1)

#Otra forma de realizar el super primo.

"""
Nombre: SuperPrimo(num)
Entradas: que reciba como entrada un número entero positivo denominado (num)
Salidas: que retorne si cumple (True) o no los requisitos (False) de número súper primo. 
Restricciones: Debe de recibir un número entero positivo diferente de cero como parámetro de entrada-
"""

def SuperPrimo(num):
    if(isinstance(num, int)):
        if(num < 0):
            return print("Error eh la entrada, el parámetro debe de ser un número positivo.")
        else:
            return esPrimo(SuperPrimo_aux(num))
    else:
        return print("Error el parámetro que dene de ingresar tiene que ser un número entrero.")

def SuperPrimo_aux(num):
    
