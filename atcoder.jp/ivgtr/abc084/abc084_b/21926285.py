a, b = map(int, input().split())
n = list(input())

if not n[a] == "-":
    print("No")
    exit()

for i in range(0, a + b):
    if not i == a:
        if n[i] == "-":
            print("No")
            exit()

print("Yes")
