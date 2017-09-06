# https://www.hackerrank.com/challenges/finding-the-percentage/problem

inputs = [ raw_input() for _ in xrange(int(raw_input())) ]
requested = raw_input()
tuples = map(lambda x: (x.split()[0], sum(map(float, x.split()[1:])) / (len(x.split()) - 1)), inputs)
dictionary = { key: value for (key, value) in tuples }
print "{0:.2f}".format(dictionary[requested])
