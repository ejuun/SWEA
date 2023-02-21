for tc in range(1, 11):
    Data, start = map(int, input().split())
    from_to = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    for i in range(0, Data, 2):
        f, t = from_to[i], from_to[i+1]
        G[f].append(t)
    #큐 생성
    queue = []
    #방문 표시하기 위한 리스트
    visited = [0] * 101
    #최단거리 체크하는 리스트
    D = [0] * 101

    #시작 지점 삽입
    queue.append(start)
    #시작점 방문 처리
    visited[start] = 1

    #큐가 빌때까지
    while queue:
        v = queue.pop(0)

        for w in G[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = 1
                D[w] = D[v] + 1
    #가장 마지막에 위치된 지점 찾기
    max_val = 0
    max_idx = 0
    for i in range(len(D)):
        if D[i]:
            if max_val <= D[i]:
                max_val = D[i]
                max_idx = i

    print(f'#{tc} {max_idx}')

