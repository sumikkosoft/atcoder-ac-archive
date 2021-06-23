a, b, c = map(int, input().split())

for _ in range(101):
    if c % 2 == 0:
        if not a == 0:
            a -= 1
            if not b == 0:
                b -= 1
            else:
                print("Takahashi")
                exit()
        else:
            print("Aoki")
            exit()
    else:
        if not b == 0:
            b -= 1
            if not a == 0:
                a -= 1
            else:
                print("Aoki")
                exit()
        else:
            print("Takahashi")
            exit()
