computers=int(input())
conn=int(input())

graph = [[] for i in range(computers+1)]
visited = [False] * (computers +1)

for i in range(conn):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

cnt = 0

def dfs(now):
    global cnt
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            cnt += 1 # 새롭게 감염된 컴퓨터 카운트
            dfs(nxt)

dfs(1)
print(cnt)