A, B, C = map(int, input().split())
N = int(input())

for i in range(N):
    if A >= B:
        B *= 2
    elif B >= C:
        C *= 2

if A < B < C:
    print("Yes")
else:
    print("No")
