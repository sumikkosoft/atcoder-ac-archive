a, b, c = map(int, input().split())
arr = sum(list(map(int, input().split())))

tmp = a * c - arr

if tmp > b:
    tmp = -1
elif tmp < 0:
    tmp = 0

print(tmp)
