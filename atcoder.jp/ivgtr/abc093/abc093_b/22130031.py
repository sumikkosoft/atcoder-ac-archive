a, b, k = map(int, input().split())
ans = list()

for i in range(a, min(b + 1, a + k)):
    if i not in ans:
        print(i)
        ans.append(i)

for i in range(max(a, b - k + 1), b + 1):
    if i not in ans:
        print(i)
        ans.append(i)
