#Martes 09/03/21

"""
Nombre: NumeroPar
Entrada: Número entero positivo
Salidas: Si es un número par True y si no lo es entonces False
Restricciones: Numero entero positivo mayor o igual a cero
"""

def NumeroPar(num):
    if(isinstance(num, int)and num >= 0):
        if(num%2)== 0:
            return True
        else:
            return False
    else:
        print("Digite un número entero positivo")

#--------------------------------------------------------------
"""
Nombre: ContarPares
Entrada: Un número entero positivo.
Salida: Cantidad de digitos pares.
Restricciones: Un numero entero positivo mayor que cero.
"""

def ContarPares(num):
    if(isinstance(num, int)and num >= 0):
        if (num == 0):
            return 1
        else:
            return ContarPares_aux(num)
    else:
        return print("Error, el parámetro (n) no cumple con las resticciones de ser un número entero positivo mayor que cero ")

def ContarPares_aux(num):
    if(num == 0):
        return 0
    elif(num % 2 == 0):
        return 1+ContarPares_aux(num // 10)
    else:
        return 0+ContarPares_aux(num // 10)
    

