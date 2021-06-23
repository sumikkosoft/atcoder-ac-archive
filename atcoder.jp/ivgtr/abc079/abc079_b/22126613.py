n = int(input())
memo = {0: 2, 1: 1}


def cul(z):
    if z not in memo:
        memo[z] = cul(z - 1) + cul(z - 2)
    return memo[z]


print(cul(n))
