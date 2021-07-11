import itertools
import copy #copy.copy()で行列のコピー
from itertools import permutations #組み合わせ
from collections import Counter #要素数え上げ
import math
import sys
from bisect import bisect_right
sys.setrecursionlimit(10**6)

N= int(input())
C = list(map(int, input().split()))
C.sort()
diff = 0
s = 0
for  i in range(N):
    if i == 0:
        diff = C[i]
        s = diff % (10**9 + 7)
    else:
        diff = diff -1 + (C[i] - C[i-1])
        s = (s * diff) % (10**9 + 7)
print(s)
