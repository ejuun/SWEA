T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    land = [list(map(int, input().split())) for _ in range(N)]

    min_val = 1000000
    #1열 ~ 마지막 열까지 진행
    for a in range(1, N):
        #세로합
        sero = 0
        for i in range(N):
            for j in range(a, N):
                sero += land[i][j]

        #가로 합 구하기
        for c in range(1, N):
            garo_up = 0
            garo_down = 0

            # 가로 윗 부분의 합 구하기
            for u in range(c):
                for g in range(a):
                    garo_up += land[u][g]

            #가로 아랫 부분의 합 구하기
            for d in range(N-c):
                for g in range(a):
                    garo_down += land[c+d][g]

            #농작물 총합의 최대값과 최솟값의 차이
            sec_sum = max(sero, garo_up, garo_down) - min(sero, garo_up, garo_down)

            if min_val > sec_sum:
                min_val = sec_sum

    print(f'#{tc} {min_val}')