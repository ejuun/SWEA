def back(i, hap):
    global ans

    if ans < hap:
        return

    if i > 12:
        if ans > hap:
            ans = hap
            return
    else:
        back(i + 1, hap + day * m[i])
        back(i + 1, hap + month)
        back(i + 3, hap + month3)
        back(i + 12, hap + year)

for tc in range(1, int(input())+1):
    day, month, month3, year = map(int, input().split())
    m = [0] + list(map(int, input().split()))

    ans = 0xffffffffff

    back(0, 0)

    print(f'#{tc} {ans}')
