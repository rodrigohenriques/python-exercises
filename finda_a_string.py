# https://www.hackerrank.com/challenges/find-a-string/problem

string = raw_input().strip()
sub_string = raw_input().strip()

def count_substring(string, sub_string):
    sub_len = len(sub_string)
    chunks = [string[i:i + sub_len] for i in range(len(string) - sub_len + 1)]
    chunks = filter(lambda x: x == sub_string, chunks)
    return len(chunks)

count = count_substring(string, sub_string)
print count
