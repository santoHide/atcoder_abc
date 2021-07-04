import math
import sys
from bisect import bisect_right
sys.setrecursionlimit(10**6)

N = int(input())

if N ==1:
    print(1)
else:
    for i in range(N):
        if i*(i+1)/2 >= N:
            print(i)
            break;
