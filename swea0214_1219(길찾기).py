for tc in range(1, 11):
    n, length = map(int, input().split())
    edge_list = list(map(int, input().split()))
    G = [[] for _ in range(200)]

    for i in range(0, len(edge_list)-1, 2):
        G[edge_list[i]].append(edge_list[i+1])

    visited = [0] * 101

    start, end = 0, 99

    visit_list = []

    def dfs(v):
        visited[v] = 1
        visit_list.append(v)
        for w in G[v]:
            if not visited[w]:
                dfs(w)

    dfs(start)

    for vertex in visit_list:
        if end  == vertex:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')
