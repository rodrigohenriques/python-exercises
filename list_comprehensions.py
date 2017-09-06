# https://www.hackerrank.com/challenges/list-comprehensions/problem
x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())

list = [[i, j, k] for i in xrange(0, x + 1) for j in xrange(0, y + 1) for k in xrange(0, z + 1)]

filtered = filter(lambda item: sum(item) != n, list)

print filtered
