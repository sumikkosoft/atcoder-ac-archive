a, b = input().split()

l = list([a * int(b), b * int(a)])

print("{}".format(sorted(l)[0]))
