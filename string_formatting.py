def print_formatted(number):
    bsize = len(bin(number))
    for i in xrange(1,number + 1):
        print "{0:{b}d} {0:{b}o} {0:{b}X} {0:{b}b}".format(i, b=bsize - 2)

number = int(raw_input())

print_formatted(number)
