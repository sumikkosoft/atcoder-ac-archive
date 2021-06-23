n = int(input())
s = list(input())
q = int(input())

pre = s[0:n]
para = s[n : 2 * n]

for _ in range(q):
    x, a, b = map(int, input().split())
    if x == 1:
        a, b = sorted([a - 1, b - 1])
        if b + 1 <= n:
            pre[a], pre[b] = pre[b], pre[a]
        elif a + 1 > n:
            para[a - n], para[b - n] = para[b - n], para[a - n]
        else:
            pre[a], para[b - n] = para[b - n], pre[a]
    else:
        pre, para = para, pre

print("".join(pre + para))
