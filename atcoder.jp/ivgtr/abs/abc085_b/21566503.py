import sys


def main():
    a = int(input())
    arr = [int(input()) for i in range(a)]
    ans = []

    for _ in range(a):
        num = max(arr)
        if num in ans:
            arr.remove(num)
        else:
            ans.append(num)
            arr.remove(num)

    print("{}".format(len(ans)))


if __name__ == "__main__":
    main()
