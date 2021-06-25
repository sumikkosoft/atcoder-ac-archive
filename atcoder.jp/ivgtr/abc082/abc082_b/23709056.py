S = list(input())
T = list(input())

s = "".join(sorted(S))
t = "".join(sorted(T, reverse=True))


if s < t:
    print("Yes")
else:
    print("No")
