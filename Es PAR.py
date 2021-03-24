#Verifica si un número es PAR.

def esPar(num):
    if(isinstance(num, int)and (num>=0)):
        if(num % 2 == 0):
            return print("True")
        else:
            return print("False")
    else:
        return print("Error, dígite un número entreo positivo.")
