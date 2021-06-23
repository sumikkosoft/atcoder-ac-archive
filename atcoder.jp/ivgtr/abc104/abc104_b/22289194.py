s = input()
if s[0] == "A" and s[2:-1].count("C") == 1:
    n = s.replace("A", "a").replace("C", "c")
    t = n.lower()
    if n == t:
        print("AC")
        exit()
print("WA")