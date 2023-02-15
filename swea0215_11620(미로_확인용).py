# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 r, c = i, j
#                 break
#     found = 0
#
#
#     def find(r, c):
#         global maze
#
#         if r < 0 or r >= N or c < 0 or c >= N or maze[r][c] == 1:
#             # return 0
#
#         if maze[r][c] == 3:
#             return 1
#
#         ret = 0
#         if maze[r][c] == 0 or maze[r][c] == 2:
#             maze[r][c] = 1
#             ret += find(r, c - 1)
#             ret += find(r, c + 1)
#             ret += find(r - 1, c)
#             ret += find(r + 1, c)
#         return ret
#
#     print(f'#{tc} {find(r,c)}')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
                break

    found = 0

    def find(r, c):
        global maze, found

        if found:
            return

        if r < 0 or r >= N or c < 0 or c >= N or maze[r][c] == 1:
            return

        if maze[r][c] == 3:
            found = 1
            return

        maze[r][c] = 1
        find(r, c - 1)
        find(r, c + 1)
        find(r - 1, c)
        find(r + 1, c)
        return

    find(r,c)

    print(f'#{tc} {found}')