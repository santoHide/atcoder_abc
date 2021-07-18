import itertools
import copy #copy.copy()で行列のコピー
from itertools import permutations #組み合わせ
from collections import Counter, defaultdict #要素数え上げ
import math
import sys
from bisect import bisect_right
from collections import deque
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
c = list(map(int, input().split()))

#ダメな例(計算量オーバー)
max_c  = 0
for  i in range(N+1-K):
  N2 = c[i:i+K]
  l = [0] * max(N2)
  k=K
  for  j in N2:
    if l[j-1] == 0:
      l[j-1] = 1
    else:
      k= k-1
  if k > max_c:
    max_c = k
print(max_c)

#正解
#defaultdictを用いて初期化
max_kind  = 0
kinds = 0
d = defaultdict(int)
for i in range(K):
  if d[c[i]] == 0:
    kinds  += 1
  d[c[i]] +=1
max_kind = max(kinds,max_kind)
for i in range(K,N):
  if d[c[i-K]] == 1:
    kinds -=1
  d[c[i-K]] -=1
  if d[c[i]] == 0:
    kinds += 1
  d[c[i]] += 1
  max_kind = max(kinds,max_kind)
print(max_kind)
