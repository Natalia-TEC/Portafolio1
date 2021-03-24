#Cuenta la cantidad de ceros que hay en un número.

def CantidadCeros(num):
    if(isinstance(num,int) and num>=0):
        if(num==0):
         return 0
        if((num%10)==0):
            return (1+CantidadCeros(num//10))
        else:
            return (CantidadCeros(num//10))
    else:
        return("Intentelo de nuevo, digite un numero entero positivo")

    
