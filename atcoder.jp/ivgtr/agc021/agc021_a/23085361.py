N = int(input())
S = list(str(N + 1))
ans = 0

ans += (len(S) - 1) * 9
ans += int(S[0]) - 1


print(ans)
