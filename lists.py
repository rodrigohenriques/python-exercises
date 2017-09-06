# Ref: https://www.hackerrank.com/challenges/python-lists/problem

N = int(raw_input())

myList = []

def printList():
    print myList

commands = {
    'insert': (lambda args: myList.insert(args[0], args[1])),
    'print': (lambda args: printList()),
    'remove': (lambda args: myList.remove(args[0])),
    'append': (lambda args: myList.append(args[0])),
    'sort': (lambda args: myList.sort()),
    'pop': (lambda args: myList.pop()),
    'reverse': (lambda args: myList.reverse())
}

inputedCommands = [raw_input() for i in xrange(N)]

for inputed in inputedCommands:
    values = inputed.strip().split(' ')
    commandName = values[0]
    args = map(int, values[1:])

    if commandName in commands:
        command = commands[commandName]
        command(args)
