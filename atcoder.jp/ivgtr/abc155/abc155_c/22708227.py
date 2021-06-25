N = int(input())
S = [input() for _ in range(N)]
tmp = dict()
stack = 0
ans = list()

for i in S:
    tmp.setdefault(i, 0)
    tmp[i] += 1
    stack = max(tmp[i], stack)

for i in tmp:
    if tmp[i] == stack:
        ans.append(i)

ans.sort()

for i in ans:
    print(i)
