n = int(input())
a,b = input().split()
tmp = ""

for i in range(n):
  tmp += a[i] + b[i]
  
print(tmp)