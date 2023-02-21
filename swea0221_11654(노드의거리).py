T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    Graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        Graph[u].append(v)
        Graph[v].append(u)
    # print(Graph) [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]
    S, G = map(int, input().split())

    queue = []
    visited= [0] * (V+1)
    D = [0] * (V+1) #출발점에서 각 정점까지의 최단거리
    #P = [0] * (V+1) #부모 노드의 위치
    #시작점을 방문하고 큐에 삽입
    queue.append(S)
    visited[S] = 1

    while queue:
        t = queue.pop(0)
        #t의 방문하지 않은 인접정점들을 모두 찾아서
        for w in Graph[t]:
            if not visited[w]:
                queue.append(w)
                # 방문처리
                visited[w] = 1
                #w = 시작점에서 t 까지 이동 거리 + 1
                D[w] = D[t] + 1
                #부모노드의 위치 저장
                #P[w] = D[t]

    print(f'#{tc} {D[G]}')


