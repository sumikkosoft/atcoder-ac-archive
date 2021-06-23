s = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if not i % 2:
        if i % 3 and i % 5:
            print("DENIED")
            exit()
print("APPROVED")
