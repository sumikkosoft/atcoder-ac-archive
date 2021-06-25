S = input()
before = S[: int(len(S) // 2)]
after = S[int(len(S) // 2) :][::-1]
ans = 0

for i in range(len(before)):
    if not before[i] == after[i]:
        ans += 1

print(ans)
