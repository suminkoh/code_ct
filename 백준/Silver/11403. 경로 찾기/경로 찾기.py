# 11403번
INF=int(1e9)

N=int(input())


#각 인접행렬 입력받고 초기화
graph=[]
for i in range(N):
  graph.append(list(map(int, input().split())))

#점화식에 따른 플로이드 워셜 알고리즘
for k in range(N):
  for a in range(N):
    for b in range(N):
      if graph[a][k] ==1 and graph[k][b] ==1:
        graph[a][b] = 1

#결과 출력
for a in range(N):
  for b in range(N):
      print(graph[a][b], end=" ")
  print()


