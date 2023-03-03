# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     farm = [list(map(int, input())) for _ in range(N)]
#     n = N // 2
#     crop_sum = 0
#     for i in range(N // 2):
#         crop_sum += sum(farm[i][n-i: n+i + 1])
#
#         crop_sum += sum(farm[-i-1][n-i: n+i + 1])
#
#     crop_sum += sum(farm[N//2])
#
#     print(f'#{tc} {crop_sum}')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    m = N // 2

    #[2] 범위
    s = e = m
    for i in range(N):
        for j in range(s, e+1):
            ans += arr[i][j]
        if i < m:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    #[1] 규칙성
    # for i in range(N):
    #     for j in range(abs(m-i), N-abs(m-i)):
    #         ans += arr[i][j]
    #
    print(f'#{tc} {ans}')