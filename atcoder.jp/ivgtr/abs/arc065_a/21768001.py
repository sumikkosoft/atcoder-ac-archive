a = input()
word = ["dream", "dreamer", "erase", "eraser"]

while True:
    flag = True

    for i in word:
        if a.endswith(i):
            a = a[: -len(i)]
            flag = False
    if flag:
        break

print("YES") if not len(a) else print("NO")
