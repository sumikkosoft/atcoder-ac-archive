N = int(input())
S = list(map(int, input().split()))

S.sort()

print(abs(S[-1] - S[0]))
