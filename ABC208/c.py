N, K = map(int, input().split())
a = list(map(int, input().split()))

if K %N == 0:
    for i in range(N):
        print(int(K/N))
else:
    b = sorted(a)
    c = b[K%N]
    for i in range(N):
        if a[i] >= c:
            print(K//N)
        else:
            print(K//N+1)
