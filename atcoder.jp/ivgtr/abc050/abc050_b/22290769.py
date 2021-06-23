n = int(input())
t = list(map(int, input().split()))
m = int(input())
sumt = sum(t)
for i in range(m):
    p, x = map(int, input().split())
    print(sumt - t[p - 1] + x)
