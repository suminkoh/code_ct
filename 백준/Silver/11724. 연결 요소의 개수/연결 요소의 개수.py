import sys
# 재귀 제한을 10,000번 혹은 1,000,000번 정도로 넉넉하게 늘려줍니다.
sys.setrecursionlimit(10**6)

# 그 아래에 기존 코드(입력, DFS 함수 등)를 작성
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for i in range(N+1)]
visited=[False]*(N+1)

for i in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(now):
    visited[now] = True
    for nt in graph[now]:
        if not visited[nt]:
            dfs(nt)


count = 0
for i in range(1, N + 1):
    if not visited[i]: # 방문 안 한 노드 = 새로운 덩어리의 시작점
        dfs(i)         # 그 덩어리에 속한 모든 노드를 True로 만들고 나옴
        count += 1     # 덩어리 개수 하나 추가!

print(count)