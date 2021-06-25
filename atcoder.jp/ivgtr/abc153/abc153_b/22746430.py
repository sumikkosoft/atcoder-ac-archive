N, K = map(int, input().split())
A = list(map(int,input().split()))


if sum(A) >= N:
    print("Yes")
else:
    print("No")
