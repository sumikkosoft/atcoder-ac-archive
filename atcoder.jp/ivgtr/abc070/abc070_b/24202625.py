A, B, C, D = map(int, input().split())
ans = min(B, D) - max(A, C)
print(ans if ans > 0 else 0)
