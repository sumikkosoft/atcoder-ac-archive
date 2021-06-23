def main():
    a = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(a):
        num = max(arr)
        if i % 2:
            ans -= num
        else:
            ans += num
        arr.remove(num)

    print("{}".format(ans))


if __name__ == "__main__":
    main()
