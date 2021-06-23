n, a, b = map(int, input().split())
arr = list(input())
_a = 0
_b = 0

for i in arr:
    if i == "a":
        if _a + _b < a + b:
            _a += 1
            print("Yes")
            continue
        else:
            print("No")
            continue
    elif i == "b":
        if _a + _b < a + b and _b < b:
            _b += 1
            print("Yes")
            continue
        else:
            print("No")
            continue
    else:
        print("No")
        continue
