S = input()
N = int(S)
T = 0

for i in S:
    T += int(i)

if N % T:
    print("No")
else:
    print("Yes")
