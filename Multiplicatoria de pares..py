#multiplicatoria pares
"""
Nombre: MultiplicatoriaPares(num)
Entradas: Num(número mayor entero positivo)
Salidas: Resultado de la multiplicación de los dígitos pares de la multiplicatoria
Resticciones: Ser entrero positivo
"""

def MultiplicatoriaPares(num):
    if(isinstance(num, int)and (num >=0 )):
        if(num == 1):
            return 1 #fin de la recursividad
        else:
            return MultiplicatoriaPares_aux(num)

def MultiplicatoriaPares_aux(num):
    if(num == 1):
        return 1 #Fin de la recursividad
    elif(num%2 == 0):
        return num *MultiplicatoriaPares_aux(num - 1)
    else:
        return 1* MultiplicatoriaPares_aux(num - 1)
    
