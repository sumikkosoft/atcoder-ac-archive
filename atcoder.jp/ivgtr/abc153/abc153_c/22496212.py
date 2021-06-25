N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

for i in range(K):
    if len(H):
        H.pop()


print(sum(H))
