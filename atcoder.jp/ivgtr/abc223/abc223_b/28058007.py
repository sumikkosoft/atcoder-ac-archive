S = input()
S_list = list(S)

shift = list()

for i in range(len(S_list)):
    shift.append(S_list[: i + 1] + S_list[i + 1 :])
    shift.append(S_list[-1 - i :] + S_list[: -1 - i])

shift.sort()

print("".join(shift[0]))
print("".join(shift[-1]))
