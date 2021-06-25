N = int(input())
i = 2
ans = dict()

while i ** 2 <= N:
    j = 2
    while i ** j <= N:
        ans[i ** j] = True
        j += 1
    i += 1

print(N - len(ans))
