#Sumarmitades 
"""
Nombre: Sumarmitades(num)
Entradas: num(número entero positivo diferente de cero)
Salidas: La suma de dos números que corresponde al dividir la mitad del número como parámetro de entrada.
Restricciones:
        Ingresar un número entero positivo.
        Si el número es largo impar, el dígito del medio se comparte para los nuevos números de izquierda a derecha.
"""
def ContarDigitos(num):
    if(isinstance(num, int)== False):
        return print("Error de tipo de dato, vuelva a intentarlo.")
    elif(num < 10):
        return 1
    else:
        return 1+ContarDigitos(num//10)


def Sumarmitades(num):
    
    tempo = num
    if(num < 0):
        num *= -1
        
    largo = ContarDigitos(num)
    
    if (largo % 2 == 0):#par
        mitadI = num // (10 ** (largo // 2))
        mitadII = num % (10 ** (largo // 2))
    else: #impar
        mitadI = num // (10 ** (largo // 2))
        mitadII = num % (10 ** ((largo // 2) + 1))
        
    if(tempo < 0):
        mitadI *= -1
        
    return print(mitadI + mitadII)
    
