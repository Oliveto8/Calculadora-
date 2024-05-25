
def ingresar_operando(numero):
    while True:
        try:
            operando = float(input(f"\nIngrese el valor para {numero}: "))
            return operando
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "\nNo se puede dividir por cero."

def factorial(a):
    if a < 0:
        return "\nNo se puede calcular el factorial de un número negativo."
    elif a == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, int(a) + 1):
            factorial *= i
        return int(factorial)
    
def calculos(a, b):
    sumar(a,b)
    restar(a,b)
    multiplicar(a,b)
    dividir(a,b)
    factorial(a)

def informar_resultados(a,b):
    print(f"\nLa suma es: {sumar(a,b)}")
    print(f"La resta es: {restar(a,b)}")
    print(f"La multiplicacion es: {multiplicar(a,b)}")
    print(f"La divicion es: {dividir(a,b)}")
    print(f"El factorial es: {factorial(a)}")