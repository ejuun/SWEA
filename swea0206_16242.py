T = int(input())
for tc in range(1, T+1):
    case = [[0 for _ in range(10)]for _ in range(10)]

    r, c, wide, height = map(int, input().split())
    n = 1
    for i in range(height):
        for j in range(wide):
            if i % 2:
                case[r+i][c+j +(wide-1-2*j)] = n
            else:
                case[r+i][c+j] = n
            n += 1

    print(f'#{tc}')
    for i in range(10):
        print(*case[i])