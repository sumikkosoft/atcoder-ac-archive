N = int(input())
A = set(input() for _ in range(N))

for i in A:
    if "!" + i in A:
        print(i)
        exit()


print("satisfiable")
