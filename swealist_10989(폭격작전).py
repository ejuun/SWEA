T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    m = [list(map(int, input().split()))for _ in range(N)]
    #중복 지점 있는지 확인용
    check_list = [[0 for _ in range(N)] for _ in range(N)]

    dr = [-1, 1, 0, 0]  # 상 하 좌 우
    dc = [0, 0, -1, 1]  # 상 하 좌 우
    #사상자 카운트
    dead = 0
    for bomb in range(M):
        r, c, size = map(int, input().split())
        for dir in range(4):
            for i in range(size+1):
                nr = r + dr[dir] * i
                nc = c + dc[dir] * i
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    break
                else:
                    #해당 자리에 1더하기
                    check_list[nr][nc] += 1
                    #만약 중복이 아니면 사상자 수 더하기
                    if check_list[nr][nc] == 1:
                        dead += m[nr][nc]
    print(f'#{tc} {dead}')
