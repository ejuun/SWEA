# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     matrix = [[0 for _ in range(N)]for _ in range(N)]
#
#     x = y = 0
#
#     dx = [0, 1, 0, -1] #우하좌상
#     dy = [1, 0, -1, 0] #우하좌상
#     i = 0
#     n = 1
#     while True:
#         matrix[x][y] = n
#         if n == N**2:
#             break
#         x += dx[i] + x
#         y += dy[i] + y
#         n += 1
#         if x < 0 or x >= N or y < 0 or y >= N or matrix[x][y] != 0:
#             x -= dx[i]+x
#             y -= dy[i]+y
#             n -= 1
#             i += 1
#             i = i % 4
#
#         for line in matrix:
#             print(*line)
#
#
#     for dir in range(1):
#         for i in range(1,k+1):
#             nx = r + dx[dir] * i
#             ny = c + dy[dir] * i
#             if ny < 0 or ny >= N:
#                 break
#             matrix[nx][ny] = n
#             n += 1
#         r = nx
#         c = ny
#     for line in matrix:
#         print(*line)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(N)]for _ in range(N)]

    #초기값 설정
    x = y = 0

    dx = [0, 1, 0, -1]#우하좌상
    dy = [1, 0, -1, 0]#우하좌상
    i = 0

    n = 1
    while True:
        matrix[x][y] = n

        if n == N ** 2:
            break

        x += dx[i]
        y += dy[i]
        n += 1

        if x >= N or y >= N or x < 0 or y < 0 or matrix[x][y] != 0:
            x -= dx[i]
            y -= dy[i]
            n -= 1

            i += 1
            i = i % 4

            x += dx[i]
            y += dy[i]
            n += 1

    print(f'#{tc}')
    for line in matrix:
        print(*line)