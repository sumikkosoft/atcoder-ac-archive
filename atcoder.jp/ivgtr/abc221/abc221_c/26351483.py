N = sorted(input(), reverse=True)
ans = 0

for i in range(1 << len(N)):
    left = ""
    right = ""
    for j in range(len(N)):
        if i & (1 << j):
            left += N[j]
        else:
            right += N[j]

    if left and right:
        a = int(left)
        b = int(right)
        ans = max(ans, a * b)

print(ans)
