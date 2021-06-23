a, b = map(int, input().split())
while True:
    if a % b < a:
        a = a % b
    else:
        if abs(a - b) < a:
            a = abs(a - b)
        else:
            break


print(a)
