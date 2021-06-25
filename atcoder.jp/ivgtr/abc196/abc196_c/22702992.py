N = int(input())


for i in range(1, 10 ** 6 + 1):
    if int(str(i) + str(i)) > N:
        print(i - 1)
        exit()
