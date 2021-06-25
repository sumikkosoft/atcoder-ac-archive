A, B, C, D = map(int, input().split())

for i in range(1, 101 * 2):
    if i % 2:
        C -= B
    else:
        A -= D
    if A <= 0 or C <= 0:
        print("Yes") if i % 2 else print("No")
        exit()
