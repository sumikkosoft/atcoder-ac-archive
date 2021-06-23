n = int(input())
c = list(map(int, input().split()))
c.sort(reverse=True)

a = sum(c[1::2])
b = sum(c[0::2])


print(b - a)
