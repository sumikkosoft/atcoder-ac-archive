a, b, c = map(int, input().split())


max = max([a, b])
_c = -1 * c

if max == 1:
    print("1")
    exit()

tmp = list()

for i in range(1, max + 1):
    if a % i == 0 and b % i == 0:
        tmp.append(i)

print(tmp[_c])
