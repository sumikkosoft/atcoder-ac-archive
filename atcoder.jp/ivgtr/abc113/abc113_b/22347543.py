n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ans = list()

for i, x in enumerate(h):
    ans.append((abs(t - x * 0.006 - a), i))

print(min(ans)[1] + 1)
