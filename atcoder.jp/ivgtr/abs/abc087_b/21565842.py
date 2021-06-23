def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    _a = 500
    _b = 100
    _c = 50

    cnt = 0

    for i1 in range(a + 1):
        for i2 in range(b + 1):
            for i3 in range(c + 1):
                if i1 * _a + i2 * _b + i3 * _c == x:
                    cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
