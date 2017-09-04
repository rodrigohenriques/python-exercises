print('Calculadora Tabajara v1.0.0')

def printResultado(n1, sinal, n2, resltado):
    print("{} {} {} = {}".format(n1, sinal, n2, resultado))

number1 = raw_input('Digite o primeiro numero : ')
operator = raw_input("Digite a operacao : ")
number2 = raw_input('Digite o segundo numero : ')

if operator == "x":
    resultado = int(number1) * int(number2)
    printResultado(number1, operator, number2, resultado)
elif operator == "/":
    resultado = float(number1) / float(number2)
    printResultado(number1, operator, number2, resultado)
elif operator == "+":
    resultado = int(number1) + int(number2)
    printResultado(number1, operator, number2, resultado)
elif operator == "-":
    resultado = int(number1) - int(number2)
    printResultado(number1, operator, number2, resultado)
else:
    print("Operador invalido: {}".format(operator))
