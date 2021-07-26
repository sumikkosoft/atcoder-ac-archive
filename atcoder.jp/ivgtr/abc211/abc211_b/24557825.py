X = [input() for _ in range(4)]
ans = ["H", "2B", "3B", "HR"]
ans.sort()
X.sort()

print("Yes") if ans == X else print("No")
