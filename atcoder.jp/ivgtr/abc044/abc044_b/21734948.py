a = input()

ans = dict()

for i in range(len(a)):
    if ans.get(a[i], 0):
        ans[a[i]] += 1
    else:
        ans[a[i]] = 0
        ans[a[i]] += 1


for n in ans.values():
    if not n % 2 == 0:
        print("No")
        exit()


print("Yes")
