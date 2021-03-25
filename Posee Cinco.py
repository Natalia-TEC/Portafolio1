#Verifica si un número posee 5.

def poseeCinco(num):
    if(num == 0):
        return False
    elif(num == 5):
        return True
    elif(num % 5 == 0):
        return True
    else:
        return poseeCinco(num//10)
    
