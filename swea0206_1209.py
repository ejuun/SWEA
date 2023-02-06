for tc in range(1, 11):
    N = 100
    T = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    #행
    m_r = 0
    for i in range(N):
        r_s = 0
        for j in range(N):
            r_s += arr[i][j]
            if m_r < r_s:
                m_r = r_s
    #열
    m_c = 0
    for i in range(N):
        c_s = 0
        for j in range(N):
            c_s += arr[j][i]
            if m_c < c_s:
                m_c = c_s

    #대각선 정방향
    m_d_r = 0
    for i in range(N):
        m_d_r += arr[i][i]
    #대각선 역방향 아래
    m_d_re = 0
    for i in range(N):
       m_d_re += arr[i][-(i+1)]


    print(f'#{tc} {max(m_r, m_c, m_d_r, m_d_re)}')
    # print(m_r)
    # print(m_c)
    #