n = list("abcdefghijklmnopqrstuvwxyz")
s = input()

for i in n:
    if i not in s:
        print(i)
        exit()

print("None")
