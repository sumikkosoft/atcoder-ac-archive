N = int(input())
S = [input() for _ in range(N)]

tmp = {}

for i in range(N):
    tmp.setdefault(S[i], 0)
    tmp[S[i]] += 1

tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)

print(tmp[0][0])
