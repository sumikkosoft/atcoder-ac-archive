import sys

a = input()

n = len(a)

for i in range(n):
    _n = "0" * i + a
    if len(_n) % 2:
        an = (len(_n) - 1) // 2
    else:
        an = len(_n) // 2
    flag = True
    for _i in range(an):
        if not _n[_i] == _n[-1 * _i - 1]:
            flag = False
    if flag:
        print("Yes")
        sys.exit()

print("No")
