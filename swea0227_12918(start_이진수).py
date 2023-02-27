def bi(n):
    num = ''
    for _ in range(4):
        if n == 0:
            num = '0' + num
        else:
            num = str(n % 2) + num
        n = n // 2
    return num

T = int(input())
for tc in range(1, T + 1):
    N, N_num = map(str, input().split())

    ans = ''
    for i in range(int(N)):

        if ord('A') <= ord(N_num[i]) <= ord('F'):
            ans += bi(int('0x'+N_num[i], 16))

        else:
            ans += bi(int(N_num[i]))

    print(f'#{tc} {ans}')

