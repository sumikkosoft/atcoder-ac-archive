a = int(input())
b = int(input())
c = int(input())
A = 500
B = 100
C = 50
x = int(input())
ans = 0

for i in range(a + 1):
    for j in range(b + 1):
        tmp = x - (A * i) - (B * j)
        if tmp >= 0 and tmp // C <= c:
            ans += 1
            continue


print(ans)
