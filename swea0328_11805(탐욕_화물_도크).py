for tc in range(1, int(input()) + 1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort(key=lambda x: x[1])

    cnt = 1

    k = 0
    if len(time) >= 2:
        for i in range(1, len(time)):
            # 이전의 종료 시점보다 다음의 시작시간이 같거나 더 늦다면
            if time[i][0] >= time[k][1]:
                cnt += 1
                k = i

    print(f'#{tc} {cnt}')