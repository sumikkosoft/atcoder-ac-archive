A, B = input().split()

x = min(len(A), len(B))

for i in range(x):
    if int(A[-1 - i]) + int(B[-1 - i]) >= 10:
        print("Hard")
        exit()

else:
    print("Easy")
