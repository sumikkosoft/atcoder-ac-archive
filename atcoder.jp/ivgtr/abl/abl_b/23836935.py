A, B, C, D = map(int, input().split())

test1 = B < C
test2 = A > D

if not (test1 or test2):
    print("Yes")
else:
    print("No")
