S = input()
tmp = 0
for i in range(len(S)):
    if S[i] == "0":
        tmp += 1
    else:
        tmp -= 1

print(len(S) - abs(tmp))
