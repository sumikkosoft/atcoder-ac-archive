N = int(input())
tmp = [0] * (N + 1)

for i in range(N - 1):
    A, B = map(int, input().split())
    tmp[A] += 1
    tmp[B] += 1

if max(tmp) == N - 1:
    print("Yes")
else:
    print("No")
