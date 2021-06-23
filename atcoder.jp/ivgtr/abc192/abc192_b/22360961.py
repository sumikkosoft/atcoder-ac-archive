s = input()
tmp = "abcdefghijklmnopqrstuvwxyz"

for i in range(1, len(s) + 1):
    if i % 2:
        if not s[i - 1] in tmp:
            print("No")
            exit()
    else:
        if s[i - 1] in tmp:
            print("No")
            exit()

print("Yes")
