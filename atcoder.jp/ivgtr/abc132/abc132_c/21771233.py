n = int(input()) // 2
arr = list(map(int, input().split()))

arr.sort()

x = arr[n] - arr[n - 1]

print(x)
