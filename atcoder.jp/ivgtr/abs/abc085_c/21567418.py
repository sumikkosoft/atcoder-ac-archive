def main():
    a, b = map(int, input().split())
    x, y, z = [10000, 5000, 1000]

    for i1 in range(a + 1):
        for i2 in range(a + 1):
            i3 = a - (i1 + i2)
            if i3 < 0:
                break
            if i1 * x + i2 * y + i3 * z == b and i1 + i2 + i3 == a:
                print(i1, i2, i3)
                exit()

    print(-1, -1, -1)


if __name__ == "__main__":
    main()
