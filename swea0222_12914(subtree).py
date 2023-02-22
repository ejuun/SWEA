T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    Edge = list(map(int, input().split()))

    P = [0] * (E + 2)
    L = [0] * (E + 2)
    R = [0] * (E + 2)

    for i in range(0, E * 2, 2):
        p, c = Edge[i], Edge[i+1]

        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c

        P[c] = p

    cnt = 0

    def inorder(v):

        if v == 0:
            return

        inorder(L[v])
        inorder(R[v])

    def subtree(v):
        if v == 0:
            return

        global cnt
        cnt += 1
        subtree(L[v])
        subtree(R[v])

    inorder(1)
    subtree(N)

    print(f'#{tc} {cnt}')