N = input()

a, b, c = N[0], N[1], N[2]

if N[0] == N[1] == N[2]:
    print(int(N))
else:
    if int(N[0]) >= int(N[1]) and int(N[0]) >= int(N[2]):
        print(int(N[0]) * 111)
    else:
        print((int(N[0]) + 1) * 111)
