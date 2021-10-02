S = input()
T = input()

if S == T:
    print("Yes")
    exit()

for i in range(0, len(S) - 1):
    tmp = list(S)
    before = tmp[i]
    after = tmp[i + 1]
    tmp[i] = after
    tmp[i + 1] = before

    if "".join(tmp) == T:
        print("Yes")
        exit()

print("No")
