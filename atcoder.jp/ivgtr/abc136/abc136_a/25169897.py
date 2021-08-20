A, B, C = map(int, input().split())
X = A - B

print(max(C - X, 0))
