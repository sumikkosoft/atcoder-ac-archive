N = int(input())
A = list(map(int, input().split()))
tmp = dict()

for i in range(N):
    if tmp.get(A[i], False):
        print("NO")
        exit()
    else:
        tmp[A[i]] = True


print("YES")
