x = list(input())
y = list()

for i in x:
    if i in y:
        print("no")
        exit()
    else:
        y.append(i)

print("yes")
