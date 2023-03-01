for tc in range(1, int(input())+1):
    N, direct = map(str, input().split())
    m = [list(map(int, input().split())) for _ in range(int(N))]
    n = int(N)
    #왼쪽
    def move():
        for i in range(n):
            j = 0
            while j != n-1:
                if m[i][j]:
                    k = j + 1
                    while m[i][k] == 0:
                        if k + 1 == n:
                            break
                        k += 1
                    #수가 같으면 j값에 x2 한 후 그 전까지 0 처리
                    if m[i][k] == m[i][j]:
                        m[i][j] += m[i][j]
                        for a in range(j+1, k+1):
                            m[i][a] = 0
                    #수가 다르면 j 앞으로 옮기기
                    elif m[i][k] != 0 and m[i][k] != m[i][j]:
                        if k != j + 1:
                            m[i][j+1], m[i][k] = m[i][k], m[i][j+1]
                    j += 1

                else:
                    k = j + 1
                    while m[i][k] == 0:
                        if k + 1 == n:
                            break
                        k += 1
                    #끝까지 0일 경우
                    if k == n-1 and m[i][k] == 0:
                        j = k
                        break
                    #끝 값이 있을 경우
                    elif k == n-1 and m[i][k] != 0:
                        m[i][j], m[i][k] = m[i][k], m[i][j]
                        j = k
                        break
                    #중간에 값이 있을 경우
                    else:
                        m[i][j], m[i][k] = m[i][k], m[i][j]
        return m

    def change_side():
        for i in range(n):
            for j in range(n//2):
                m[i][j], m[i][n-1-j] = m[i][n-1-j], m[i][j]
        return m

    def change_u_b():
        for i in range(n):
            for j in range(n):
                if i < j:
                    m[i][j], m[j][i] = m[j][i], m[i][j]
        return m

    if direct == 'right':
        change_side()
        move()
        change_side()

    elif direct == 'up':
        change_u_b()
        move()
        change_u_b()

    elif direct == 'down':
        change_u_b()
        change_side()
        move()
        change_side()
        change_u_b()

    else:
        move()

    print(f'#{tc}')
    for line in m:
        print(*line)