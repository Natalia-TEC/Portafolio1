""" Cantidas de dígitos que son divisibles por tres, de formas diferentes. """


#------------------------------------------------------------------------------------------------
#Cantidad de dígitos del número que son divisibles entre tres, utlizando una auxiliar.
def divisibletres(num):
    if(isinstance(num,int) and num>=0):
      return divisiblestres_aux(num)
    else:
        return "Vuelva a intentarlo, digite un numeros que sea un entero positivo"

def divisiblestres_aux(num):
    if(num == 0):#Fin de la recursividad
        return 0
    elif((num%10)%3==0):
        return 1 + divisiblestres_aux(num//10)      
    else:
        return divisiblestres_aux(num//10)

#------------------------------------------------------------------------------------------------
#Cantidad de dígitos del número que son divisibles entre tres.

def DivisibleTres(num):
    if(isinstance(num,int) and num>=0):
        if(num==0):
            return 0
        if((num%10)%3==0):
            return 1+DivisibleTres(num//10)
        else:
            return DivisibleTres(num//10)
    else:
        return ("Vuelva a intentarlo, digite un numero entero positivo")

#------------------------------------------------------------------------------------------------    
#Otra forma de realizar la divisibilidad por 3

def TresDivisible(num):
    if(isinstance(num,int) and num>=0):
        return TresDivisible_aux(num,0)
    else:
        return ("Vuelva a intentarlo, digite un numero entero positivo")


def TresDivisible_aux(numVerified,res):
    if(numVerified==0):
        return res
    if((numVerified%10)%3==0):
        return TresDivisible_aux(numVerified//10 ,res+1)
    else:
        return TresDivisible_aux(numVerified//10,res)   


    
