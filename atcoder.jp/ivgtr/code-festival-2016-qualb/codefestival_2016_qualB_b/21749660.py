n, a, b = map(int, input().split())
s = list(input())

total = a + b
patht = 0
pathb = 0

for i in range(n):
    m = s[i]

    if m == "a" and patht < total:
        patht += 1
        print("Yes")
    elif m == "b" and patht < total and pathb < b:
        patht += 1
        pathb += 1
        print("Yes")
    else:
        print("No")
