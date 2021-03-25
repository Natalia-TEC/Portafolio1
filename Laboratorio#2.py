#Laboratorio 2
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
        return primo(suma)#Fin de la recursión de pila.
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
            return print("Error en la entrada, el parámetro debe de ser un número positivo.")
        else:
            #resul=SuperPrimo_auz(num)
            #resultado= primo(resul)
            #return (resultado)
            return primo(SuperPrimo_aux(num))#forma más sencilla de realizarlo.
        
    else:
        return print("Error el parámetro que dene de ingresar tiene que ser un número entrero.")

def SuperPrimo_aux(num):
    if(num==0):
        return 0 #Fin de la recursión
    else:
        if(((num % 10) % 2) == 0):
            return SuperPrimo_aux(num // 10)
        else:
            return ((num % 10)+ SuperPrimo_aux(num // 10))

#Unir ascendentes

"""
Nombre: unirAscendente(num)
Entradas: (num) un número entero cualquiera
Salidas: retornar un nuevo número, que recorriendo de derecha a izquierda el número de entrada, se forme por dígitos 
que sean mayores o iguales al anterior que forma parte del nuevo número, siempre la unidad formará parte del nuevo número.
Restricciones: Debe conservar el signo de la entrada.
                Recibir un número entero cualquiera.
                Siempre la unidad formará parte del nuevo número.
"""

def unirAscendentes(num):
    if(isinstance(num, int)):
        if(num < 0):
            return -1 * unir_aux((num * -1), 0, 0)
        else:
            return unir_aux(num, 0, 0)
    else:
        return print("Error en la entrada, vuelava a intentarlo.")

def unir_aux(num, potencia, digito):
    if(num == 0): #Fin de la recursión.
        return 0
    else:
        if(potencia == 0):
            digito = (num % 10)
            return ((num % 10) + unir_aux(num // 10, potencia + 1, digito))
        
        if((num % 10) >= digito):
            valor = (num % 10) * (10 ** potencia)
            return (valor + unir_aux(num // 10, potencia + 1, num % 10))
        
        else:
            return unir_aux(num // 10, potencia, digito)

#Factores Número.

"""
Nombre: factoresNumero(num)
Entradas: (num) un número entero positivo.
Salidad: retorne la cantidad de pares de dos números (factores) que multiplicados lo generan
Restricciones: Debe de ingresar un número entero positivo.
               Los factores deben ser diferentes de uno y el mismo.   
"""
    
def factoresNumero(num):
    if(isinstance(num, int)):
        divisores = contarDivisores(num)
        if(divisores <= 1):
            return divisores
        else:
            return divisores // 2
    else:
        return print("Error en el parámetro de entrada.")

def contarDivisores(num):
    if(isinstance(num, int)):
        if(num > 2):
            return contarDiv_aux(num, 2)
        else:
            return 0
    else:
        return print("Error, el parámetro de entrada debe de ser un número entero")

def contarDiv_aux(num, contador):
    if((num - 1) == contador): #Fin de la recursión.
        return 0
    else:
        if((num % contador) == 0):
            return 1 + contarDiv_aux(num, contador + 1)
        else:
            return 0 + contarDiv_aux(num, contador + 1)

#Números compadres

"""
Nombre: numerosCompadres(num1, num2)
Entradas:(num1, num2) recibe dos números enteros positivos.
Salidas: retorna True si comparten algún “slice” de tres dígitos (de num2 a num1) entre ellos.
Restricciones: Debe recibir números enteros positivos.
               Debe de compartir 3 digitos en la misma posición.
"""
def numerosCompadres(num1, num2):
    if(isinstance(num1, int)and isinstance(num2, int)):
        numMayor = Mayor(num1, num2)
        numMenor = menor(num1, num2)
        return numeros_aux(numMayor, numMenor)
    else:
        return print("Error, los parámetros de entrada deben de ser números enteros positivos.")

def numeros_aux(numMayor, numMenor):
    if(ContarDigitos_v2(numMenor) < 3):
        return False
    else:
        if(pertenece(numMayor, (numMenor % 1000))):
            return True
        else:
            return numeros_aux(numMayor, numMenor // 10)

def pertenece(numero, parte):
    if(numero == 0):
        return False
    else:
        if((numero % 1000) == parte):
            return True
        else:
            return (pertenece((numero // 10), parte))

def Mayor(a, b):
    if(a >= b):
        return a
    else:
        return b

def menor(a, b):
    if(a < b):
        return a
    else:
        return b    

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
