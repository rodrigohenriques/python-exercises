# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(raw_input())
arr = map(int, raw_input().split())
distinct = list(set(arr))
distinct.sort()
print distinct[-2]
