a = int(input())
arr = list(map(int, input().split()))
ans = 0

while all(i % 2 == 0 for i in arr):
    if sum(arr) % 2:
        break
    arr = [i // 2 for i in arr]
    ans += 1

print(ans)
