S = input()
T = list(input())

if S == "".join(T[:-1]):
    print("Yes")
else:
    print("No")
