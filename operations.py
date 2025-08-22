def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b  

def power(a, b):
    return a ^ b
    #No funciona como debería, la forma correcta a aplicar sería la siguiente comentada  
    #return a**b

def square_root(x):
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list)

def maximum(list):
    return min(list) 
    #No funciona como debería, regresa el mínimo y no el máximo
    #return min(list) 


if __name__ == "__main__":

    print("start test")

    print("end test")

    print("suma =", add (-5,3))
    #El resultado esperado sería que no emprimiera por ser tipo str, aún así lo concateno
    print("suma =", add ("a","b"))

    #Se detuvo el código y no emprimió nada al detectar un tipo str
    #print("resta =", subtract("a","b"))
    print("resta =", subtract(-2,-2))
    print("resta =", subtract(8,-10))

    print("multiplicación =", multiply(-2,10))
    print("multiplicación =", multiply(3,41))
    #Una posible salida algebráica sería ab, pero para el programa no debería imprimir por ser de tipo str
    #print("multiplicación =", multiply("a","b"))

    #Se detuvo el programa porque no se puede dividir entre cero
    #print("división =", divide(1,0))
    print("división =", divide(10,-100))

    #No haca matemáticamente bien la función
    print("potencia =", power(10,2))
    print("potencia =", power(2,0))

    print("raiz cuadrada =", square_root(9))
    #Se detiene otra vez la ejecución del código y nos da un mensaje de error matemático
    #print("raiz cuadrada =", square_root(-10))

    print("promedio =", average([1,2,3,4,5]))
    #Se detiene el código ya que encuentra la suma con str algo no soportable
    #print("promedio =", average([-1,2,-3,4,"b"]))

    #Hace mal la función, regresa el mínimo esperando el máximo
    #print("maximo =", maximum([1,10,100,-1,3]))
    #Detiene la ejecución del código por no soportar la suma entre entero y str
    #print("maximo =", maximum(["a",10,10,10]))


    print("end test")
