N = input()

A = 0

for i in list(N):
    A += int(i)

N = int(N)
if N % A == 0:
    print("Yes")
else:
    print("No")
