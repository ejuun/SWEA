T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    m = [list(map(int, input().split()))for _ in range(N)]
    for i in range(M):
        bomb_list = [list(map(int, input().split()))for _ in range(M)]

    dr = [-1, 1, 0, 0] #상 하 좌 우
    dc = [0, 0, -1, 1] #상 하 좌 우

    dead = 0
    for a in range(M):
        for i in range(N):
            for s in range(1, bomb_list[a][-1]+1):
                for dir in range(4):
                    nr = bomb_list[a][0] + dr[dir] * s
                    nc = bomb_list[a][1] + dc[dir] * s
                    if nr < 0 or nr > N and nc < 0 or nc > N:
                        break
                    dead += m[nr][nc]
                    print(nr,nc,m[nr][nc])
                print()

    print(f'#{tc} {dead}')