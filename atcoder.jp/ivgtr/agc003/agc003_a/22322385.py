s = input()
flag = True

if s.count("N"):
    if not s.count("S"):
        flag = False
if s.count("S"):
    if not s.count("N"):
        flag = False
if s.count("W"):
    if not s.count("E"):
        flag = False
if s.count("E"):
    if not s.count("W"):
        flag = False

if flag:
    print("Yes")
else:
    print("No")
