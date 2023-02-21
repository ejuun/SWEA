T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    Graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        Graph[u].append(v)
        Graph[v].append(u)

    S, G = map(int, input().split())

    queue = []
    visited = [0] * (V + 1)
    # 시작점을 방문하고 큐에 삽입
    queue.append(S)
    visited[S] = 1

    while queue:
        t = queue.pop(0)
        # t의 방문하지 않은 인접정점들을 모두 찾아서
        for w in Graph[t]:
            if not visited[w]:
                queue.append(w)
                # w 방문 함과 동시에 거리 표시
                visited[w] = visited[t] + 1

    if visited[G]:
        visited[G] -= 1
    print(f'#{tc} {visited[G]}')