T = int(input())
for tc in range(1, T+1):
    N = int(input())
    omok = [list(map(str, input())) for _ in range(N)]

    result = False
    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':
                cnt = 1
                #가로 검사
                for k in range(1,N):
                    if 0 <= j+k < N:
                        if omok[i][j+k] == 'o':
                            cnt += 1
                        else:
                            break
                if cnt >= 5:
                    result = True
                    break
                else:
                    cnt = 1
                #세로 검사
                for k in range(1, N):
                    if 0 <= i + k < N:
                        if omok[i+k][j] == 'o':
                            cnt += 1
                        else:
                            break
                if cnt >= 5:
                    result = True
                    break
                else:
                    cnt = 1
                #대각 검사(\)
                for k in range(1, N):
                    if 0 <= i+k < N and 0 <= j+k < N:
                        if omok[i+k][j+k] == 'o':
                            cnt += 1
                        else:
                            break
                if cnt >= 5 :
                    result = True
                    break
                else:
                    cnt = 1
                #대각 검사(/)
                for k in range(1, N):
                    if 0 < i + k < N and 0 <= j-k < N:
                        if omok[i+k][j-k] == 'o':
                            cnt += 1
                        else:
                            break
                if cnt >= 5:
                    result = True
                    break
                else:
                    cnt = 1
        if result:
            break

    if result:
        result = 'YES'
    else:
        result = 'NO'

    print(f'#{tc} {result}')