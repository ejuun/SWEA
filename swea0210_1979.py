T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    maze = [list(map(int, input().split()))for _ in range(N)]

    lenK_cnt = 0
    for i in range(N):
        # 가로 길이 K인것 검색
        cnt = 0
        for j in range(N):
            if maze[i][j] == 1:
                cnt += 1
                if cnt == K:
                    #마지막 열이거나 다음 나올 값이 0 이면 길이가 K이므로
                    if j == N-1 or maze[i][j+1] == 0:
                        lenK_cnt += 1
            #다음 길이 없다면 길이 0으로 초기화
            else:
                cnt = 0

    #세로 길이 K인거 검색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if maze[j][i] == 1:
                cnt += 1
                if cnt == K:
                    #마지막 행이거나 다음 나올 값이 0이면 길이가 K이므로
                    if j == N-1 or maze[j+1][i] == 0:
                        lenK_cnt += 1
            #다음 길이 없다면 길이 0으로 초기화
            else:
                cnt = 0

    print(f'#{tc} {lenK_cnt}')