S = input()

for i in range(0, len(S) + 1):
    _S = i * "0" + S
    if _S[::-1] == _S:
        print("Yes")
        exit()

print("No")
