N = input()
O = list()
X = list()
ans = 0

for i in range(len(N)):
    if N[i] == "o":
        O.append(str(i))
    if N[i] == "x":
        X.append(str(i))


def check(e):
    for j in O:
        if j not in e:
            return False
    for j in X:
        if j in e:
            return False

    return True


for i in range(10000):
    s = str(i).zfill(4)

    if check(s):
        ans += 1


print(ans)
