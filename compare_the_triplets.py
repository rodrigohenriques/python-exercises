import sys

def solve(a, b):
    zipped = zip(a, b)
    results = map(compare, zipped)
    return reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), results)

def compare(tup):
    if (tup[0] > tup[1]):
        return (1, 0)
    elif (tup[1] > tup[0]):
        return (0, 1)
    else:
        return (0, 0)

alices = map(int, raw_input().strip().split(' '))
bobs = map(int, raw_input().strip().split(' '))

result = solve(alices, bobs)
print " ".join(map(str, result))
