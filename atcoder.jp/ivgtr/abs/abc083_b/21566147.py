def main():
    a, b, c = map(int, input().split())
    stack = []
    for i in range(a):
        num = i + 1
        s = str(num)
        array = list(map(int, s))
        if b <= sum(array) <= c:
            stack.append(num)
    print("{}".format(sum(stack)))


if __name__ == "__main__":
    main()
