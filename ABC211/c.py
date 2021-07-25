#動的計画法
S = input()
T = "chokudai"
dp = [[0]*9 for i in range(len(S)+1)]

dp[0][0] = 1
for i in range(1,len(S)+1):
  for j in range(9):
    if j==0:
      dp[i][j] = 1
    else:
      if S[i-1] == T[j-1]:
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) %(1e9+7)
      else:
        dp[i][j] = dp[i-1][j]

print(int(dp[len(S)][8]))
