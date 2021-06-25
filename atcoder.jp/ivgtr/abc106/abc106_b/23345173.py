import math

N = int(input())
ans = 0

for i in range(1, N + 1):
    if i % 2:
        tmp = {}
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                tmp.setdefault(j, True)
                tmp.setdefault(i // j, True)
        if len(tmp) == 8:
            ans += 1
print(ans)
