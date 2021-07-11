#ユーザー解説から
#URL:https://yunix-kyopro.hatenablog.com/entry/2021/07/11/020240?_ga=2.121161536.9506465.1625937519-1301098457.1625937519#f-cd9f4786
from collections import queue

[N, Q] = [int(x) for x in input().split()]

# グラフの初期化
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    [a, b] = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)

  # 深さを記録するリスト
depth_vec = [-1 for _ in range(N+1)]

# 1を根とする根付き木を作り、各頂点の深さを記録する
queue = deque()
queue.append((1, 0))
while len(queue) > 0:
    (node, depth) = queue.pop()
    depth_vec[node] = depth
    for child in graph[node]:
        if depth_vec[child] >= 0:
            continue
        queue.append((child, depth+1))

    # クエリに解答する
for query in range(Q):
  [c, d] = [int(x) for x in input().split()]
  if (depth_vec[c] + depth_vec[d]) % 2 == 0:
      print("Town")
  else:
      print("Road")
