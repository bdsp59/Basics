
import math


def somar(a: float, b: float):
    return a + b

def subtrair(a: float, b: float):
    return a - b

def multiplicar(a: float, b: float):
    return a*b

def dividir(a: float, b: float):
    if b == 0:
        return "Error"
    return a/b

def raiz(a: float, b: float):
    return math.pow(a, (1/b))

def potencia(a: float,b: float):
    return math.pow(a, b)
    

def calculadora(tipo: str, primeiro_termo: float, segundo_termo: float):
    if tipo == "soma":
        resultado = somar(primeiro_termo, segundo_termo)
    elif tipo == "subtração":
        resultado = subtrair(primeiro_termo, segundo_termo)
    elif tipo == "multiplicação":
        resultado = multiplicar(primeiro_termo, segundo_termo)
    elif tipo == "divisão":
        resultado = dividir(primeiro_termo, segundo_termo)
    elif tipo == "raiz":
        resultado = raiz(primeiro_termo, segundo_termo)
    elif tipo == "potencia":
        resultado = potencia(primeiro_termo, segundo_termo)
    else:
        return "Error"

    return resultado

def operacao():
    primeiro = int(input("Entre com o primeiro termo: "))
    segundo = int(input("Entre com o segundo termo: "))

    tipo = input("Entre com a função a ser realizada: ")

    print(f"O resultado da {tipo} de {primeiro} com {segundo} é {calculadora(tipo, primeiro, segundo)}")

if __name__ == "__main__":
    operacao()
