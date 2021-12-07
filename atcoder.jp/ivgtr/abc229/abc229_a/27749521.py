S = [input() for _ in range(2)]

tmp = 0

for i in range(len(S)):
    for j in S[i]:
        if j == "#":
            tmp += 1

if tmp > 2:
    print("Yes")
    exit()
else:
    if S[0][0] != S[1][1]:
        print("Yes")
        exit()
print("No")
