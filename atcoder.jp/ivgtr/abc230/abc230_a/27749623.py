N = int(input())

if N > 41:
    print("AGC{}".format(str(N + 1).zfill(3)))
else:
    print("AGC{}".format(str(N).zfill(3)))
