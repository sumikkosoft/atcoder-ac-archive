N = int(input())
A = list(map(int, input().split()))
ans = 0
tmp = [0 for _ in range(201)]

for i in A:
    tmp[i % 200] += 1

for i in tmp:
    if i - 1 > 0:
        ans += i * (i - 1) // 2

print(ans)
