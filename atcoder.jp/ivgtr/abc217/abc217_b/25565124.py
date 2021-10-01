N = 3
tmp = ["ARC", "AGC", "AHC", "ABC"]

for _ in range(N):
    x = input()
    tmp.remove(x)

print(tmp[0])
