s = input()
a = 0
b = 0

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == "1":
            a += 1
        else:
            b += 1
    else:
        if s[i] == "0":
            a += 1
        else:
            b += 1

print(min(a, b))
