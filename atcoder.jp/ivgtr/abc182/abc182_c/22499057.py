N = list(map(int, list(input())))

tmp = sum(N) % 3

if tmp == 0:
    print(0)
else:
    if len(N) > 1:
        if tmp == 1:
            for i in N:
                if i % 3 == 1:
                    print(1)
                    exit()
            if len(N) > 2:
                print(2)
                exit()
            else:
                print(-1)
                exit()
        else:
            for i in N:
                if i % 3 == 2:
                    print(1)
                    exit()
            if len(N) > 2:
                print(2)
                exit()
            else:
                print(-1)
                exit()
    else:
        print(-1)
