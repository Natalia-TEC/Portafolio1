#Fibonacci de un número.

def fibonacci(num):
    if(isinstance(num,int)and (num>=0)):
        if(num == 0):
            return 0
        elif(num == 1):
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)
    else:
        print("ERROR: el parámetro n no cumple con la restricción de ser un número entero positivo.")
        
