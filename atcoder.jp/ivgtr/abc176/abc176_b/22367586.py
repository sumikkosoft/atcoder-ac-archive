N = input()
ans = 0
for i in range(len(N)):
    ans += int(N[i])
print("Yes") if ans % 9 == 0 else print("No")
