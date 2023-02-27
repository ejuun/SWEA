T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    n = N // 2
    crop_sum = 0
    for i in range(N // 2):
        crop_sum += sum(farm[i][n-i: n+i + 1])

        crop_sum += sum(farm[-i-1][n-i: n+i + 1])

    crop_sum += sum(farm[N//2])

    print(f'#{tc} {crop_sum}')