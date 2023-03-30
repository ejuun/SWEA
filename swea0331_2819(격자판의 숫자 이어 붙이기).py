def back(x, y):
    if len(arr) == 7:
        ans.add(tuple(arr))
        return

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < 4 and 0 <= ny < 4:
            arr.append(p[nx][ny])
            back(nx, ny)
            arr.pop()

for tc in range(1, int(input())+1):
    p = [list(map(int, input().split())) for _ in range(4)]

    ans = set()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        for j in range(4):
            arr = [p[i][j]]
            back(i, j)

    print(f'#{tc} {len(ans)}')
