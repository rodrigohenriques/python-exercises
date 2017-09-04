def multiplicar(n1, n2):
    return int(n1) * int(n2)

def dividir(n1, n2):
    return float(n1) / float(n2)

def somar(n1, n2):
    return int(n1) + int(n2)

def subtrair(n1, n2):
    return int(n1) - int(n2)

def obterFuncaoDeCalcular(sinal):
    if sinal == "x":
        return multiplicar
    elif sinal == "/":
        return dividir
    elif sinal == "+":
        return somar
    elif sinal == "-":
        return subtrair
