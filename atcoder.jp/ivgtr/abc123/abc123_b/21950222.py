import math

a = [input() for _ in range(5)]


tmp = 0

for i in range(len(a)):
    if 10 > 10 - int(a[i][-1]) >= tmp:
        tmp = 10 - int(a[i][-1])

    a[i] = int(math.ceil(int(a[i]) / 10) * 10)


print(sum(a) - tmp)
