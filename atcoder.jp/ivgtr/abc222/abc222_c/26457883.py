N, M = map(int, input().split())
A = [list(input()) for _ in range(2 * N)]
tmp = dict()

for i in range(2 * N):
    tmp.setdefault(2 * N - i, i)

for i in range(M):
    tmp2 = sorted(tmp.items(), key=lambda x: x[0], reverse=True)
    tmp3 = dict()
    for j in range(0, 2 * N, 2):
        left = A[tmp2[j][1]][i]
        right = A[tmp2[j + 1][1]][i]
        left_score = tmp2[j][0]
        right_score = tmp2[j + 1][0]

        if (
            (left == "C" and right == "P")
            or (left == "P" and right == "G")
            or (left == "G" and right == "C")
        ):
            tmp3.setdefault(left_score + 1000, tmp2[j][1])
            tmp3.setdefault(right_score, tmp2[j + 1][1])

        elif (
            (left == "P" and right == "C")
            or (left == "C" and right == "G")
            or (left == "G" and right == "P")
        ):
            tmp3.setdefault(left_score, tmp2[j][1])
            tmp3.setdefault(right_score + 1000, tmp2[j + 1][1])

        else:
            tmp3.setdefault(left_score, tmp2[j][1])
            tmp3.setdefault(right_score, tmp2[j + 1][1])

    tmp = tmp3

ans = sorted(tmp.items(), key=lambda x: x[0], reverse=True)

for i in ans:
    print(i[1] + 1)
