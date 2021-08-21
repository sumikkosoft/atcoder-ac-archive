import collections
import itertools

S, K = input().split()
K = int(K)

S = list(S)

S.sort()

tmp = list(itertools.permutations(S))
aa = list(collections.OrderedDict.fromkeys(tmp))
print("".join(aa[K - 1]))
