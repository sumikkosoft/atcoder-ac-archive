a = int(input())
arr = list()
for _ in range(a):
    arr.append(list(map(int, input().split())))

flag = True

for i in range(a):
    time, x, y = arr[i]
    if i > 0:
        _t, _x, _y = arr[i - 1]
    else:
        _t, _x, _y = [0, 0, 0]

    time = abs(time - _t)
    kyori = abs(x - _x) + abs(y - _y)

    if kyori > time or not time % 2 == kyori % 2:
        flag = False

print("{}".format("Yes" if flag else "No"))
