N = int(input())
J = ["AC", "WA", "TLE", "RE"]
tmp = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}

for i in range(N):
    tmp[input()] += 1

for i in J:
    print(i + " x " + str(tmp[i]))
