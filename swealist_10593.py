T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]

    K = N
    di = [-1, 1, 0, 0] #상하 좌우
    dj = [0, 0, -1, 1] #상하 좌우

    max_sum = 0

    for i in range(N):
        for j in range(N):
            total_sum = m[i][j]
            for k in range(1, K):
                for dir in range(4):
                    ni = i + di[dir] * k
                    nj = j + dj[dir] * k
                    if 0 <= ni <= (N-1) and 0 <= nj <= (N-1):
                        total_sum += m[ni][nj]
            if max_sum < total_sum:
                max_sum = total_sum

    print(f'#{tc} {max_sum}')

