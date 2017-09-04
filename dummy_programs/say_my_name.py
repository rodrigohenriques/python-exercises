def ePar( number ):
    resto = number % 2

    if resto == 0:
        return True
    else:
        return False

numero = 0

while numero < 5:
    numero = numero + 1

    if ePar(numero):
        print("Hello par " + str(numero))
    else:
        print("Hello impar " + str(numero))
