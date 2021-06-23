def main():
    a = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    while True:
        flag = False
        for i in arr:
            if i % (2 ** (cnt + 1)):
                flag = False
                break
            else:
                flag = True
        if flag:
            cnt += 1
        else:
            break
    print(cnt)


if __name__ == "__main__":
    main()