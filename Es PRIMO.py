#Verifica si el número es PRIMO.

"""
Nombre: esPrimo(num)
Entradas:num(un número entero positivo)
Salidas: True si todos dígitos del números son primos y False si algun dígitos del número no es primo.
Restricciones: Ser números enteros positivos.
"""

def esPrimo(num):
    if(isinstance(num, int)and (num >=0 )):
        return esPrimo_aux(num,2)
    else:
        return print ("Error: el parámetro no cumple con las restricciones, vuelva a intentarlo de nuevo.")

def esPrimo_aux(num, cont):
    if(num == cont):
        return True
    elif (num % cont == 0):
        return False
    else:
        return esPrimo_aux(num, cont+1)

#------------------------------------------------------------

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
