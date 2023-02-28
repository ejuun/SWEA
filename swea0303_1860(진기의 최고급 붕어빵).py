for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    #손님 : N명, M초당 K개의 붕어빵 생성
    customer = list(map(int, input().split()))

    result = 'Possible'

    bbang = [0] * 11112

    for i in range(len(bbang)):
        if i >= M:
            bbang[i] = K * (i // M)

    for cus in customer:
        for i in range(cus, len(bbang)):
            bbang[i] -= 1

    for minus in bbang:
        if minus < 0:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')

#손님 리스트 생성해서 정렬 하고
#m 시간내에 k명 이상의 손님이 있을 경우 impossible

