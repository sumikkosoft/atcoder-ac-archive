N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=True)
print(sum(H[K:])) if len(H) > K else print(0)
