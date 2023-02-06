T = int(input())
for tc in range(1, T+1):
    case = [[0 for _ in range(10)]for _ in range(10)]

    r, c, wide, height = map(int, input().split())
    n = 1
    for i in range(c, c+wide): #열
        for j in range(r, r+height): #행
            case[j][i] = n
            n += 1

    print(f'#{tc}')
    for i in range(10):
        print(*case[i])