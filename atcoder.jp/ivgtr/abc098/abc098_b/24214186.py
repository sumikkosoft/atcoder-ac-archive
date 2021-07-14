import collections

N = int(input())
S = list(input())
ans = 0

for i in range(N - 1):
    before, after = collections.Counter(S[: i + 1]), collections.Counter(S[i + 1 :])
    tmp = 0
    for j in before.keys():
        for k in after.keys():
            if j == k:
                tmp += 1
    ans = max(ans, tmp)

print(ans)
