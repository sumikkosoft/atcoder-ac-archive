n = input()
t = input()

for i in range(len(t)):
    n = n[1:] + n[0]
    if t == n:
        print("Yes")
        exit()

print("No")
