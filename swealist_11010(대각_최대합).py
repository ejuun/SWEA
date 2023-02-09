T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0

    dx = [-1, 1, -1, 1]#좌상 우상 좌하 우하
    dy = [1, 1, -1, -1]#좌상 우상 좌하 우하

    for i in range(N):#행
        for j in range(N): #열
            dia_num = 0 #각 원소(?)에 대해 대각값 초기화
            for dir in range(4):
                for k in range(1, N): #모든 대각합 구하기 위해 길이 변동
                    nx = i + dx[dir] * k
                    ny = j + dy[dir] * k
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        break
                    else:
                        dia_num += num[nx][ny]
            dia_num += num[i][j]#길이 1부터하여 본인 포함 안돼서 포함
            if max_num < dia_num:
                max_num = dia_num
    print(f'#{tc} {max_num}')

