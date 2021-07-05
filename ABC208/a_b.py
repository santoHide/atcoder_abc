import itertools
from itertools import permutations #組み合わせ
from collections import Counter #要素数え上げ
import math
import sys
from bisect import bisect_right
sys.setrecursionlimit(10**6)

#a
A, B = map(int, input().split())

if 6*A >=B and A <= B:
    print("Yes")
else:
    print("No")

#b
P = int(input())

flag = 1
n=0
a = 0
while(flag):
    flag2 = 1
    for i in range(100):
        a = math.factorial(i)
        if a >= P:
            if a > P:
                n = n+1
                P = P - math.factorial(i-1)
                break
            else:
                flag= 0
                n = n+1
                break
print(n)
