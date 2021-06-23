a = list(input())
arr = ["753"]
ans = 0

for i in range(len(a) - 2):
    arr.append(a[i] + a[i + 1] + a[i + 2])

arr.sort()

index = arr.index("753")

if index == len(arr) - 1:
    ans = int(arr[index]) - int(arr[index - 1])
elif index == 0:
    ans = int(arr[index + 1]) - int(arr[index])
elif int(arr[index + 1]) - int(arr[index]) > int(arr[index]) - int(arr[index - 1]):
    ans = int(arr[index]) - int(arr[index - 1])
else:
    ans = int(arr[index + 1]) - int(arr[index])

print(ans)
