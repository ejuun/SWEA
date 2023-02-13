def power(n, m):
    if m == 1:
        return n
    else:
        return n * power(n, m-1)

for tc in range(1, 11):
    tc_case = int(input())
    n, m = map(int, input().split())

    print(f'#{tc} {power(n, m)}')