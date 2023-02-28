for tc in range(1, 11):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for col in range(N):
        magnet = []
        for row in range(N):
            if m[row][col]:
                magnet.append(m[row][col])
        if len(magnet) > 1:
            for i in range(len(magnet)-1):
                if magnet[i] == 1 and magnet[i+1] == 2:
                    cnt += 1

    print(f'#{tc} {cnt}')
