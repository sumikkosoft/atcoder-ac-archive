N = int(input())
P = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if not i + 1 == P[i]:
        if cnt > 1:
            print("NO")
            exit()
        cnt += 1

print("YES")
