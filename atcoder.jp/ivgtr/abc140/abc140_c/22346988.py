n = int(input())
b = list(map(int, input().split()))
b.append(b[-1])
ans = [b[0]]

for i in range(1, n):
    ans.append(min(b[i - 1], b[i]))


print(sum(ans))
