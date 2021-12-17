N = int(input())
S = list(map(int, input().split()))


ans = 0

for i in range(N):
    flag = True
    for a in range(1, 1001):
        for b in range(1, 1001):
            x = 4 * a * b + 3 * a + 3 * b
            if x == S[i]:
                flag = False
    if flag:
        ans += 1


print(ans)
