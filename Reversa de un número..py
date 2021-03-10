#Martes 09/03/21

"""
Nombre: ReversaNumero
Entradas: Número entero mayor o igual a cero.
Salidas:El número en orden inverso a su representación original
Restricciones: Un número entero positiv mayor o igual a cero.  
"""
#---------------------------------------------------------------
def ContarDigitos_v2(num):
    if(isinstance(num, int) == False):
        return print("Error de tipo de dato")
    elif (num == 0):
        return 0
    else:
        return ContarDigitos_aux(num)

def ContarDigitos_aux(num):
    if(num == 0):
        return 0
    else:
        return 1 + ContarDigitos_aux(num // 10)
#--------------------------------------------------------------

def ReversaNumero(num):
    if(isinstance(num, int)):
        if (num >= 0):
            if (num <=10 ):
                return (num)
            else:
                return ReversaNumero_aux(num, ContarDigitos_v2(num))
        else:
            return print("Debe ser un número mayor o igual que cero")
    else:
        return print("Error, debe de ingresar un número positivo mayor o igual a cero")

def ReversaNumero_aux(num, Largo):
    if(Largo == 0):
        return 0
    else:
        return ((num % 10) * (10 ** (Largo - 1)) + ReversaNumero_aux(num // 10, Largo - 1))
        
