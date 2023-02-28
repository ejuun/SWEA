for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    flag = [list(map(str, input())) for _ in range(N)]

    total_cnt = 10000000
    w_cnt = 0
    for i in range(N-2):
        for w in range(M):
            if flag[i][w] != 'W':
                w_cnt += 1
        b_cnt = 0
        for j in range(i+1, N-1):
            for b in range(M):
                if flag[j][b] != 'B':
                    b_cnt += 1
            r_cnt = 0
            for k in range(j+1, N):
                for r in range(M):
                    if flag[k][r] != 'R':
                        r_cnt += 1

            cnt = w_cnt + b_cnt + r_cnt
            if total_cnt > cnt:
                total_cnt = cnt

    print(f'#{tc} {total_cnt}')