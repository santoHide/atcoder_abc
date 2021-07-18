#a
N, A, X, Y = map(int, input().split())

if N >A:
  print(A*X +(N-A)*Y)
else:
  print(N*X)

  #b
  N = int(input())
s = input()

for i in range(N):
  if s[i] == "1":
    j = i
    break

if (j+1) %2 ==0:
  print("Aoki")
else:
  print("Takahashi")
