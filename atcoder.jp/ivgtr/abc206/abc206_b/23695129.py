N = int(input())

tmp = 0


for i in range(1, int(10 ** 9) + 1):
    tmp += i
    if tmp >= N:
        print(i)
        exit()
