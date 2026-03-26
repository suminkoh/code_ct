import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N=int(input())

graph = [[] for i in range(N+1)]
parent = [0] * (N + 1)

for i in range(N-1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)


def dfs(now):
    # 별도의 visited[now] = True 가 필요 없음! 
    # 대신 parent[now]에 값이 있으면 이미 방문한 것으로 간주함.
    
    for nxt in graph[now]:
        if parent[nxt] == 0:   # 아직 부모가 없다면 (=방문 전이라면)
            parent[nxt] = now  # "내(now)가 너(nxt)의 부모야"라고 기록
            dfs(nxt)

# 4. 루트인 1번부터 시작 (1번은 부모가 없으므로 미리 체크)
parent[1] = 1 
dfs(1)

# 5. 2번 노드부터 부모 출력
for i in range(2, N + 1):
    print(parent[i])