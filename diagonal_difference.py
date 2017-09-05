# Sample Input
#
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
#
# Sample Output
# 15

import sys

n = int(raw_input().strip())
a = []

for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

def getDiagonal(array, secondary = None):
    if secondary is None:
        initialIndex = 0
        nextIndex = lambda i: i + 1
    else:
        initialIndex = n - 1
        nextIndex = lambda i: i - 1

    tup = reduce(lambda acc, item: (nextIndex(acc[0]), item[acc[0]] + acc[1]), a, (initialIndex, 0))
    return tup[1]

primaryDiagonal = getDiagonal(a)
secondaryDiagonal = getDiagonal(a, True)

diff = primaryDiagonal - secondaryDiagonal

print str(abs(diff))
