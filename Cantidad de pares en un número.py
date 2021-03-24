#La cantidad de dígitos pares que hay en un número.

def CantidadPares(num):
    if(isinstance(num,int) and num>=0):
        return CantidadPares_aux(num,0)
    else:
        return ("Vuelva a intentarlo, digite un numero entero positivo")


def CantidadPares_aux(numVerified,res):
    if(numVerified==0):
        return res
    if(numVerified%2==0):
        return CantidadPares_aux(numVerified//10 ,res+1)
    else:
        return CantidadPares_aux(numVerified//10,res)
