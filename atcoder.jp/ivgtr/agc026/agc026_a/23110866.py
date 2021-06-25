N = int(input())
S = list(map(int, input().split()))
left = 0
right = 0
ans = 0
tmp = 0

while right != N:
    if S[left] == S[right]:
        tmp += 1
        right += 1
    elif tmp > 1:
        ans += tmp // 2
        tmp = 0
        left = right
    else:
        tmp = 0
        left = right

if tmp > 1:
    ans += tmp // 2

print(ans)
