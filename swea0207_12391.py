#문제 정독!!!!
T = int(input())
for tc in range(1, T+1):
    P, pa, pb = map(int, input().split())

    def binarysearch(end, key):
        start = 1
        cnt = 0
        while start <= end:
            middle = int((start + end) / 2)
            if middle < key:
                start = middle
                cnt += 1
            elif middle > key:
                end = middle
                cnt += 1
            else:
                cnt += 1
                break
        return cnt

    a = binarysearch(P, pa)
    b = binarysearch(P, pb)

    print(a, b)

    print(f'#{tc}', end=' ')
    if a > b:
        print('B')
    elif b > a:
        print('A')
    else:
        print(0)