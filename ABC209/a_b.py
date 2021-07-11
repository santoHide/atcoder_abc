#a
N, X = map(int, input().split())

if N >= X:
    print(0)
else:
    print(X -N +1)

#b
N, X = map(int, input().split())
l = list(map(int, input().split()))


if sum(l)- N//2 > X:
    print("No")
else:
    print("Yes")
