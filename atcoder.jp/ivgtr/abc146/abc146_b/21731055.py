a = int(input())
arr = list(input())

x = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
tmp = list()

for i in arr:
    n = x.index(i)
    n += a
    if n < 26:
        tmp.append(x[n])
    else:
        n -= 26
        tmp.append(x[n])

print("{}".format("".join(tmp)))
