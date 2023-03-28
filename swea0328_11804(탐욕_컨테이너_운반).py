for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    goods = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)

    weight = 0

    i = k = 0
    while i < M:
        if truck[i] >= goods[k]:
            weight += goods[k]
            i += 1

        k += 1

        if k == N:
            break

    print(f'#{tc} {weight}')