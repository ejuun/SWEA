for tc in range(1, int(input())+1):
    N, X = map(int, input().split())

    f = [list(map(int, input().split())) for _ in range(N)]

    able = 0
    #가로 갯수 세기
    for i in range(N):
        if max(f[i]) - min(f[i]) <= 1:
            m = min(f[i])
            leng = 0
            for j in range(N):
                if f[i][j] == m:
                    leng += 1
                    if leng == X:
                        if f[i][0] > m and f[i][N-1] > m:
                            break
                        else:
                            able += 1
                            break
                else:
                    leng = 0
    #세로 갯수 세기

    #1.전치행렬로 변환
    for i in range(N):
        for j in range(N):
            if i < j:
                f[i][j], f[j][i] = f[j][i], f[i][j]

    #2. 가로(세로) 갯수 세기
    for i in range(N):
        if max(f[i]) - min(f[i]) <= 1:
            m = min(f[i])
            leng = 0
            for j in range(N):
                if f[i][j] == m:
                    leng += 1
                    if leng == X:
                        if f[i][0] > m and f[i][N - 1] > m:
                            break
                        else:
                            able += 1
                            break
                else:
                    leng = 0

    print(f'#{tc} {able}')