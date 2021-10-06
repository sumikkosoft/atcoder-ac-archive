N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = sum([abs(a - b) for a, b in zip(A, B)])

if diff <= K:
    if K % 2 == diff % 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
