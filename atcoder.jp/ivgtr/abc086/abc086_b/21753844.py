import math

a,b = input().split()

z = int(a + b)

if math.sqrt(z).is_integer():
  	print("Yes")
else:
  print("No")