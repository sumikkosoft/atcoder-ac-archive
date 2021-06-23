a, b = map(int, input().split())
l = list()
for i in range(a):
    l.append(input())

l.sort()

print("{}".format("".join(l)))
