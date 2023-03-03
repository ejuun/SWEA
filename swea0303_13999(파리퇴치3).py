for tc in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    def catch(i, j):
        death_cross = fly[i][j]
        death_dia = fly[i][j]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        dix = [-1, 1, 1, -1] #1시 5시 7시 11시
        diy = [1, 1, -1, -1]

        for dir in range(4):
            for k in range(1, M):
                nx = i + dx[dir] * k
                ny = j + dy[dir] * k
                if 0 <= nx < N and 0 <= ny < N:
                    death_cross += fly[nx][ny]

        for dir in range(4):
            for l in range(1, M):
                nix = i + dix[dir] * l
                niy = j + diy[dir] * l
                if 0 <= nix < N and 0 <= niy < N:
                    death_dia += fly[nix][niy]

        return max(death_cross, death_dia)

    max_death = 0
    for i in range(N):
        for j in range(N):
            cnt = catch(i, j)
            if max_death < cnt:
                max_death = cnt

    print(f'#{tc} {max_death}')