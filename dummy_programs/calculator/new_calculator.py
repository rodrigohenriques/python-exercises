
import ope

print('Calculadora Tabajara v2.0.0')

number1 = raw_input('Digite o primeiro numero : ')
operator = raw_input("Digite a operacao : ")
number2 = raw_input('Digite o segundo numero : ')

funcaoDeCalcular = ope.obterFuncaoDeCalcular(operator)

if funcaoDeCalcular is None:
    print("Operador invalido: {}".format(operator))
else:
    resultado = funcaoDeCalcular(number1, number2)
    print("Resultado: {} {} {} = {}".format(number1, operator, number2, resultado))
