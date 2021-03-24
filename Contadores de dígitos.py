#Contador de dígitos

def ContarDigitos(num):
    if(isinstance(num, int)and == False):
        return print("Error de tipo de dato")
    elif(num == 0):
        return (0)
    else:
        return 1+ContarDigitos(num // 10)
        
#------------------------------------------------------------------
    
def ContadorDigitos(num):
    if(isinstance(num, int) == False):
        return print("Error de tipo de dato")
    elif (num < 10):
        return 1
    else:
        return 1+ContadorDigitos(num // 10)
            
            

#-------------------------------------------------------------------
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
  
