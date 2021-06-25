S = input()
N = int(input())

tmp = 0


for i in range(len(S)):
    if S[i] == "1":
        tmp += 1
    else:
        if tmp >= N:
            print("1")
        else:
            print(S[i])
        exit()

print("1")
