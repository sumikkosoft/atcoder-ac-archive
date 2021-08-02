import bisect

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
b_len = len(B)

ans = float("inf")

for i in A:
    index = bisect.bisect_left(B, i)
    if index == 0:
        ans = min(abs(i - B[index]), ans)
    elif index == b_len:
        ans = min(abs(i - B[index - 1]), ans)
    else:
        ans = min(abs(i - B[index - 1]), abs(i - B[index]), ans)

print(ans)
