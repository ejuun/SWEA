def divisor(n, d):
    cnt = 0
    while n % d == 0:
        n = n/d
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    number = int(input())
    a = divisor(number, 2)
    b = divisor(number, 3)
    c = divisor(number, 5)
    d = divisor(number, 7)
    e = divisor(number, 11)
    print(f'#{tc} {a} {b} {c} {d} {e}')