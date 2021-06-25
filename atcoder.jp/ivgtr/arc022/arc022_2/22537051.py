N = int(input())
P = list(map(int, input().split()))
tmp = {i: True for i in range(1, max(P) + 1)}

ans = 0
rt, lt = 0, 0
while rt < N:
    if tmp[P[rt]]:
        tmp[P[rt]] = False
        rt += 1
        ans = max(ans, rt - lt)
    elif rt == lt:
        rt += 1
        lt += 1
    else:
        tmp[P[lt]] = True
        lt += 1


print(ans)
