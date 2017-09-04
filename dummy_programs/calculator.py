print('Calculadora Tabajara v1.0.0')

def multiplicar(n1, n2):
    return int(n1) * int(n2)

def dividir(n1, n2):
    return float(n1) / float(n2)

def somar(n1, n2):
    return int(n1) + int(n2)

def subtrair(n1, n2):
    return int(n1) - int(n2)

def obterFuncaoDeCalcular(sinal):
    if operator == "x":
        return multiplicar
    elif operator == "/":
        return dividir
    elif operator == "+":
        return somar
    elif operator == "-":
        return subtrair

number1 = raw_input('Digite o primeiro numero : ')
operator = raw_input("Digite a operacao : ")
number2 = raw_input('Digite o segundo numero : ')

funcaoDeCalcular = obterFuncaoDeCalcular(operator)

if funcaoDeCalcular is None:
    print("Operador invalido: {}".format(operator))
else:
    resultado = funcaoDeCalcular(number1, number2)
    print("Resultado: {} {} {} = {}".format(number1, operator, number2, resultado))
