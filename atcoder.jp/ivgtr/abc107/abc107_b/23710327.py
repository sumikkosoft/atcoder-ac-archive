H, W = map(int, input().split())
Bord = []
Check = [True] * W

for i in range(H):
    w = list(input())
    if "#" in w:
        Bord.append(w)
    for j in range(W):
        if w[j] == "#":
            Check[j] = False

L = len(Bord)
Arr = [[] for _ in range(L)]


for i in range(L):
    for j in range(W):
        if not Check[j]:
            Arr[i].append(Bord[i][j])


for i in Arr:
    print("".join(i))
