N = list(input())

tmp = N[0]
flag1 = True
flag2 = True

for i in range(1, len(N)):
    if not tmp == N[i]:
        flag1 = False
    if not str(int(tmp) + 1)[-1] == N[i]:
        flag2 = False
    tmp = N[i]



if flag1 or flag2:
    print("Weak")
else:
    print("Strong")
