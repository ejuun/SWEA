from collections import deque

for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())

    G = [[] for _ in range(N + 1)]
    D = [0xfffff] * (N + 1)
    D[0] = 0

    for _ in range(E):
        s, e, weight = map(int, input().split())
        G[s].append((e, weight))

    queue = deque()
    queue.append(0)

    while queue:
        u = queue.popleft()

        for v, weight in G[u]:
            if D[v] > D[u] + weight:
                D[v] = D[u] + weight
                queue.append(v)

    print(f'#{tc} {D[N]}')