N = int(input())
L = list(map(int, input().split()))
ans = 0
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if not L[i] == L[j] and not L[j] == L[k] and not L[i] == L[k]:
                if L[i] + L[j] > L[k] and L[k] + L[j] > L[i] and L[i] + L[k] > L[j]:
                    ans += 1

print(ans)
