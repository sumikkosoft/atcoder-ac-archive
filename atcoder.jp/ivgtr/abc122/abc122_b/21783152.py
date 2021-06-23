n = input()


def check(str):
    if str == "A" or str == "G" or str == "C" or str == "T":
        return True
    else:
        return False


ans = 0
tmp = 0
for i in range(len(n)):
    if check(n[i]):
        tmp += 1
    else:
        if ans < tmp:
            ans = tmp
        tmp = 0

print(max(ans, tmp))
