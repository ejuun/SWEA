T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    #가장 큰 값의 위치 구해서 처음부터 가장 큰값전까지의 차이값 더하고
    #최댓값까지 제거하고
    #다시 남은 값 중에서 가장큰 값 구해서 처음부터 가장 큰 값 전까지의 차이값 더해서
    #마지막에 다다르는 방법
    earn = 0
    i = 0
    a = 0
    max_idx = price.index(max(price))
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

    print(f'#{tc} {earn}')