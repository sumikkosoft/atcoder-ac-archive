A, B, C, D = map(int, input().split())
x = 0
for i in range(1, int(10 ** 5) + 1):
    A += B
    x += C
    if x * D >= A:
        print(i)
        exit()

print(-1)
