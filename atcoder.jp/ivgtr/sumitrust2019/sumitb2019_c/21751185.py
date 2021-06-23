n = int(input())

x = int(n / 100)
y = n % 100

if x * 5 >= y:
    print("1")
else:
    print("0")
