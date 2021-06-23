bingo = list()
for _ in range(3):
    bingo.append(list(map(int, input().split())))
a = int(input())
arr = list()
for _ in range(a):
    arr.append(int(input()))

p = [
    [bingo[0][0], bingo[0][1], bingo[0][2]],
    [bingo[1][0], bingo[1][1], bingo[1][2]],
    [bingo[2][0], bingo[2][1], bingo[2][2]],
    [bingo[0][0], bingo[1][0], bingo[2][0]],
    [bingo[0][1], bingo[1][1], bingo[2][1]],
    [bingo[0][2], bingo[1][2], bingo[2][2]],
    [bingo[0][0], bingo[1][1], bingo[2][2]],
    [bingo[0][2], bingo[1][1], bingo[2][0]],
]

for i1 in p:
    if len(set(i1) & set(arr)) == 3:
        print("Yes")
        exit()


print("No")
