S = input()

before = S[:2]
after = S[2:]

yymm = False
mmyy = False

if 0 < int(after) < 13:
    yymm = True

if 0 < int(before) < 13:
    mmyy = True


if yymm:
    if mmyy:
        print("AMBIGUOUS")
    else:
        print("YYMM")
else:
    if mmyy:
        print("MMYY")
    else:
        print("NA")
