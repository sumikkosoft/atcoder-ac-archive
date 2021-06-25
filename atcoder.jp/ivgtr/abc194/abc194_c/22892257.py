N = int(input())
A = list(map(int, input().split()))
ans = 0

tmp = {i: 0 for i in range(-200, 201)}

for i in A:
    tmp[i] += 1


for i in range(-200, 201):
    for j in range(i + 1, 201):
        ans += (i - j) ** 2 * tmp[i] * tmp[j]

print(ans)
