N = int(input())
tmp = dict()
for i in range(N):
    S = input()
    tmp[S] = True

print(len(tmp.keys()))
