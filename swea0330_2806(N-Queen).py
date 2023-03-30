def nQueen(k):
    global ans

    if k == N:
        ans += 1

    for i in range(N):
        if used[i]:
            continue
        if not promising(k, i):
            continue
        used[i] = 1
        cols[k] = i
        nQueen(k + 1)
        used[i] = 0


def promising(r, c):
    for i in range(r):
        if abs(i - r) == abs(cols[i] - c):
            return False
    return True


for tc in range(1, int(input()) + 1):
    N = int(input())
    ans = 0

    # 행 방문 기록용 배열
    used = [0] * N
    # 열 방문 기록용 배열
    cols = [0] * N

    nQueen(0)
    print(f'#{tc} {ans}')