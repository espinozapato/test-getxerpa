class parametersCalculadora: #Define estructura de la operacion
    def __init__(self):
        self.operador = ""
        self.num2 = 0

def zero(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 0  
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num
    
def one(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 1  
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num
    
def two(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 2  
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num
    
def three(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 3  
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num
    
def four(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 4  
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num
    
def five(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 5  
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num
    
def six(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 6  
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num

def seven(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 7  
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num
    
def eight(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 8  
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num

def nine(*args): #Devuelve el numero referenciado o imprime el calculo de la operacion
    num = 9 
    if(args):
        print(calculate(num, args[0]))
    else:    
        return num

def plus(num): #Define valores de operador + y segundo numero 
    operation = parametersCalculadora()
    operation.operador = "+"
    operation.num2 = num
    return operation

def minus(num): #Define valores de operador - y segundo numero 
    operation = parametersCalculadora()
    operation.operador = "-"
    operation.num2 = num
    return operation

def times(num): #Define valores de operador * y segundo numero    
    operation = parametersCalculadora()
    operation.operador = "*"
    operation.num2 = num
    return operation

def divided_by(num): #Define valores de operador / y segundo numero    
    operation = parametersCalculadora()
    operation.operador = "/"
    operation.num2 = num
    return operation

def calculate(num1, operation): #Resuelve y retorna el calculo de la operacion
    if operation.operador == "+":
        return num1 + operation.num2
    elif operation.operador == "-":
        return num1 - operation.num2
    elif operation.operador == "*":
        return num1 * operation.num2
    elif operation.operador == "/":
        if operation.num2 != 0:
            return round(num1 / operation.num2)
        else:
            return('No se puede dividir entre cero!!!')
    

#Examples

#four(times(five())) # imprime 20
#one(plus(eight())) # imprime 9
#seven(minus(three())) # imprime 4
#nine(divided_by(three())) # imprime 3
#seven(divided_by(zero()))