from collections import deque

s = input()
tmp = deque()
flag = False

for i in range(len(s)):
    if s[i] == "R":
        flag = not flag
        continue

    if flag:
        if len(tmp) > 0 and tmp[0] == s[i]:
            tmp.popleft()
        else:
            tmp.appendleft(s[i])
    else:
        if len(tmp) > 0 and tmp[-1] == s[i]:
            tmp.pop()
        else:
            tmp.append(s[i])

if flag:
    tmp.reverse()


print("".join(tmp))
