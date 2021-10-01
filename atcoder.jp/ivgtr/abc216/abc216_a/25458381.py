N, K = map(int, input().split("."))


if 0 <= K <= 2:
    print(str(N) + "-")
elif 3 <= K <= 6:
    print(N)
else:
    print(str(N) + "+")
