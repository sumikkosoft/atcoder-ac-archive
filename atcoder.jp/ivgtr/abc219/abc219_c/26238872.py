from string import ascii_lowercase

X = input()
N = int(input())
S = [input() for _ in range(N)]

char_dic = {}
reversed_char_dic = {}

for i, c in enumerate(ascii_lowercase):
    char_dic[X[i]] = c
    reversed_char_dic[c] = X[i]

str_list = []

for s in S:
    tmp = ""
    for j in range(len(s)):
        tmp += char_dic[s[j]]

    str_list.append(tmp)

str_list.sort()

for s in str_list:
    tmp = ""
    for j in range(len(s)):
        tmp += reversed_char_dic[s[j]]

    print(tmp)
