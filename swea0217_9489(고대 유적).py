T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split()))for _ in range(N)]

    cnt_list = []

    for i in range(N):
        for j in range(M):
            cnt = 0
            if matrix[i][j] == 1:
                cnt += 1
                n = 1
                # 오른쪽에 길이 있을 경우
                if j+n < M and matrix[i][j+n] == 1:
                    #끝까지 이동
                    while True:
                        if j+n >= M or matrix[i][j+n] == 0:
                            break
                        else:
                            n += 1
                            cnt += 1
                    cnt_list.append(cnt)
                #아래쪽에 길이 있을 경우
                elif i + n < N and matrix[i+n][j] == 1:
                    #끝까지 이동
                    while True:
                        if i + n >= N or matrix[i+n][j] == 0:
                            break
                        else:
                            n += 1
                            cnt += 1
                    cnt_list.append(cnt)
                else:
                    cnt_list.append(cnt)

    max_num = -1
    for num in cnt_list:
        if max_num < num:
            max_num = num
    print(f'#{tc} {max_num}')