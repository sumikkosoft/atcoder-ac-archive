N = int(input())
D = list()
for _ in range(N):
    d1, d2 = map(int, input().split())
    D.append(d1 == d2)

for i in range(N - 2):
    if D[i] and D[i + 1] and D[i + 2]:
        print("Yes")
        exit()

print("No")
