T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    profit = 0
    max_price = price[-1]
    for i in range(N-2, -1, -1):
        if max_price < price[i]:
            max_price = price[i]
        else:
            profit += max_price - price[i]
    print(f'#{tc} {profit}')

    # while True:
    #     if price[i] <= price[i+1]:
    #         while price[i] <= price[i+1]:
    #             i += 1
    #             if i == len(price) - 1:
    #                 break
    #         for j in range(a, i):
    #             earn += price[i] - price[j]
    #     a = i + 1
    #     i = a
    #     if i >= len(price) - 1:
    #         break

    # print(f'#{tc} {earn}')