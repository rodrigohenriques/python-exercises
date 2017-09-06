# https://www.hackerrank.com/challenges/python-tuples/problem

n = int(raw_input())
integer_list = map(int, raw_input().split())

t = reduce(lambda acc, item: acc + (item,), integer_list, ())

print hash(t)
