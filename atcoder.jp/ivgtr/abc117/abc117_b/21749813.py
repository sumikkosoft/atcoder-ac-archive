a = int(input())
s = list(map(int, input().split()))

maxs = max(s)
s.remove(maxs)
sums = sum(s)

if sums > maxs:
    print("Yes")
else:
    print("No")
