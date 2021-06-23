h, w = map(int, input().split())
tb = "##"
for i in range(w):
    tb += "#"

print(tb)
x = list()
for _ in range(h):
    x.append("#" + input() + "#")

for i in x:
    print(i)

print(tb)
