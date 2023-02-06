T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_neibor = 0
    i_idx = 0
    j_idx = 0
    for i in range(N):
        for j in range(N):
            neibor = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                  neibor += arr[ni][nj]
            if max_neibor < neibor:
                max_neibor = neibor
                i_idx = ni
                j_idx = nj
    print(f'#{tc} {i_idx} {j_idx-1} {max_neibor}')