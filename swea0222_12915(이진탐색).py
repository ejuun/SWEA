def inorder(v):
    global i
    if v > N:
        return

    inorder(v * 2)
    G[v] = i
    i += 1
    inorder(v * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G = [0] * (N+1)
    i = 1

    inorder(1)
    print(G)
    print(f'#{tc} {G[1]} {G[N//2]}')

