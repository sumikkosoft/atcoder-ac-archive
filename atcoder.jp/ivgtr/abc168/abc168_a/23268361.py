N = list(input())

if N[-1] in ["0", "1", "6", "8"]:
    print("pon")
elif N[-1] == "3":
    print("bon")
else:
    print("hon")
