T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    land = [list(map(int, input().split())) for _ in range(N)]

    # ㅏ 형식
    min_sum = 100000000

    for i in range(1, N):
        for j in range(1, N):
            sero = 0
            garo_up = 0
            garo_down = 0
            sec_sum = 0
            # 세로 합
            for s in range(N):
                for e in range(j):
                    sero += land[s][e]
            # 가로 위 합
            for u in range(i):
                for p in range(j, N):
                    garo_up += land[u][p]
            # 가로 아래 합
            for d in range(i, N):
                for o in range(j, N):
                    garo_down += land[d][o]

            sec_sum = max(sero, garo_up, garo_down) - min(sero, garo_up, garo_down)

            if min_sum > sec_sum:
                min_sum = sec_sum

    print(f'#{tc} {min_sum}')
