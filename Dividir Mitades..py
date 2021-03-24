#Dividir mitades
"""
Nombre: Dividirmitades(num)
Entradas:num(un número entero)
Salidas:La impresión del número que corresponde al dividir la mitad del número como parámetro de entrada.
Restricciones:
            Ser números enteros mayor que cero.
            Si el largo es impar el dígito del medio se comparte para los números de izquierda a derecha.      
"""
def ContarDigitos(num):
    if(isinstance(num, int)== False):
        return print("Error de tipo de dato, vuelva a intentarlo.")
    elif(num < 10):
        return 1
    else:
        return 1+ContarDigitos(num//10)
    

def Dividirmitades(num):
    
    tempo = num
    if(num < 0):
        num *= -1
        
    largo = ContarDigitos(num)
    
    if (largo % 2 == 0):#Cantidad de digítos par
        mitadI = num // (10 ** (largo // 2))
        mitadII = num % (10 ** (largo // 2))
    else: #Cantidad de digítos impar
        mitadI = num // (10 ** (largo // 2))
        mitadII = num % (10 ** ((largo // 2) + 1))
        
    if(tempo < 0):
        mitadI *= -1
        
    return print(mitadI, mitadII)
