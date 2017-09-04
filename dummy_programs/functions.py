def sayHello():
    print("Hello")

def digaOla():
    print("Ola")

def sayHelloTo(nome):
    print("Hello " + nome)

def digaOlaParaNVezes(nome, quantasVezes):
    for contador in range(0, quantasVezes):
        print(str(1 + contador) + ". Hello " + nome)

funcao = digaOla

funcao()
sayHello()
sayHelloTo("Jefferson")
sayHelloTo("Tayrone")
digaOlaParaNVezes("Vinicius", 5)
digaOlaParaNVezes("Guilherme", 3)
