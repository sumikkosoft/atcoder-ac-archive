def main():
    a,b = map(int, input().split())
    s = a * b
    
    if(s % 2):
      v = "Odd"
    else:
      v = "Even"


    print(v)


if __name__ == "__main__":
    main()
