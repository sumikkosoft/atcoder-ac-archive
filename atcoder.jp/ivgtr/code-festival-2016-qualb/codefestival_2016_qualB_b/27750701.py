N, A, B = map(int, input().split())
S = input()

tuuka = 0
b = 0

for i in range(N):
    if S[i] == "a":
        if A + B > tuuka:
            tuuka += 1
            print("Yes")
        else:
            print("No")
    elif S[i] == "b":
        if A + B > tuuka and b < B:
            b += 1
            tuuka += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
