s = input()
before = 0
after = 0

for i in range(len(s)):
    if s[i] == "A":
        before = i
        break
for i in reversed(range(len(s))):
    if s[i] == "Z":
        after = i + 1
        break

print(after - before)
