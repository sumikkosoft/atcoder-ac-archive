import sys


def main():
    a = input()
    word = ["dream", "dreamer", "erase", "eraser"]
    word_len = list(map(len, word))

    while True:
        flag = False
        for i in word:
            if a.endswith(i):
                flag = True
                a = a[: -len(i)]
                break

        if not len(a):
            print("YES")
            sys.exit()
        elif not flag:
            print("NO")
            sys.exit()


if __name__ == "__main__":
    main()
