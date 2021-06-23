n = int(input())
arr = list(map(int, input().split()))


arr.sort()
ans = arr[0]
for i in range(n - 1):
    ans = (ans + arr[i + 1]) / 2


print(ans)
