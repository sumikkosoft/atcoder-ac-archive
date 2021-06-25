A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp = [0] * (10 ** 3 + 1)

for i in a:
    tmp[i - 1] += 1
for i in b:
    tmp[i - 1] += 1

ans = []

for i in range(len(tmp)):
    if tmp[i] == 1:
        ans.append(i + 1)

print(*ans)
