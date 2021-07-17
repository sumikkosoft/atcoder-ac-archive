import collections

N, K = map(int, input().split())
C = list(map(int, input().split()))

jisyo = dict(collections.Counter(C[:K]))
ans = len(jisyo)

for i in range(N - K):
    if jisyo[C[i]] == 1:
        jisyo.pop(C[i])
    else:
        jisyo[C[i]] -= 1
    jisyo.setdefault(C[i + K], 0)
    jisyo[C[i + K]] += 1
    ans = max(ans, len(jisyo))

print(ans)
