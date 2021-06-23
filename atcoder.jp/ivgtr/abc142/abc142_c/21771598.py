n = int(input())
arr = list(map(int, input().split()))
tmp = dict()
ans = list()

for i in range(n):
    tmp[i + 1] = arr[i]
    ans.append(0)

for i, k in tmp.items():
    ans[k - 1] = str(i)


print("{}".format(" ".join(ans)))
