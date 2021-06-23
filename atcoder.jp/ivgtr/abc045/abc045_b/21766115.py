a = input()
b = input()
c = input()
arr = {"a": a, "b": b, "c": c}
n = "a"

while True:
    if len(arr[n]) > 0:
        x = arr[n][0:1]
        arr[n] = arr[n][1:]
        n = x
    else:
        print(n.upper())
        exit()
