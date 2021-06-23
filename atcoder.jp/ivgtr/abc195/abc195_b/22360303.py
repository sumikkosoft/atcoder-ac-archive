a, b, w = map(int, input().split())
w *= 1000
ans = list()

for i in range(1, 10 ** 6 + 1):
    if a * i <= w <= b * i:
        ans.append(i)

if len(ans):
    print("{} {}".format(min(ans), max(ans)))
else:
    print("UNSATISFIABLE")
