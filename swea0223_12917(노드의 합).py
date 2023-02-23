T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    G = [0] * (N+1)

    for _ in range(M):
        node, value = map(int, input().split())
        G[node] = value

    def postorder(v):
        if v > N:
            return
        postorder(v*2)
        postorder(v*2+1)
        if not G[v]:
            if v * 2 + 1 <= N:
                G[v] = G[v*2] + G[v*2+1]
            else:
                G[v] = G[v*2]
    postorder(1)

    print(f'#{tc} {G[L]}')