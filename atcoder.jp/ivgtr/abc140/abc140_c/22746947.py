N = int(input())
B = [float("inf")] + list(map(int, input().split())) + [float("inf")]

ans = []

for i in range(1, N + 1):
    ans.append(min(B[i], B[i - 1]))


print(sum(ans))
