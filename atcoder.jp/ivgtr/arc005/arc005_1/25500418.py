N = int(input())
X = list(input().split())
ans = 0

A = "TAKAHASHIKUN"
B = "Takahashikun"
C = "takahashikun"

X[-1] = X[-1][:-1]

for i in X:
    if i == A or i == B or i == C:
        ans += 1


print(ans)
