import itertools
from itertools import permutations
from collections import Counter
import math
import sys
from bisect import bisect_right
sys.setrecursionlimit(10**6)

N = int(input())
l = list(map(int, input().split()))
a = list(Counter(l).values())
s = 0
for i in range(len(a)):
    s = s+ (N -a[i])*a[i]
    N = N - a[i]
print(s)