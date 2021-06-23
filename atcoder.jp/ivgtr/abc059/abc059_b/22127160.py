a = input()
b = input()
x = sorted({a, b})

if a == b:
    print("EQUAL")
elif len(a) == len(b):
    if x[0] == b:
        print("GREATER")
    elif x[0] == a:
        print("LESS")
else:
    if len(a) > len(b):
        print("GREATER")
    else:
        print("LESS")
