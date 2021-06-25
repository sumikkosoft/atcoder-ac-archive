N, A, B = map(int, input().split())
ans = 0
if abs(A - B) % 2 == 0:
    ans = abs(A - B) // 2
else:
    ans = min(
        (abs(abs(N - A) + abs(N - B)) + 1) // 2, (abs(abs(1 - A) + abs(1 - B)) + 1) // 2
    )


print(ans)
