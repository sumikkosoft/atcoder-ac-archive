S = list(input())
T = input()
if "".join(S) == T:
    print("Yes")
    exit()

for i in range(1, len(S)):
    tmp = "".join(S[-1 * i :]) + "".join(S[: len(S) - i])
    if tmp == T:
        print("Yes")
        exit()

print("No")
