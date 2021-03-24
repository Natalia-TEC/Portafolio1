#Factorial de un número

def factorial(n):
    if(isinstance(n, int) and (n>=0)):
        if(n == 0):
            return 1 #Fin de la recursión
        else:
            return n * factorial(n - 1)
    else:
        print("Error: el parámetro n no cumple con la restricción de que sea un número entero positivo")

