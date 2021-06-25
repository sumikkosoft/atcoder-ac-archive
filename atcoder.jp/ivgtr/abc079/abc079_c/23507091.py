S = list(input())
m = ["+", "-"]
o = 7


for i in m:
    for j in m:
        for k in m:
            if int(S[0]) + int(i + S[1]) + int(j + S[2]) + int(k + S[3]) == 7:
                print(S[0] + i + S[1] + j + S[2] + k + S[3] + "=7")
                exit()
