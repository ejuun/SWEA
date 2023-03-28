def back(cnt, change):
    global max_val
    if cnt == change:
        price_able = int(''.join(price))
        if max_val < price_able:
            max_val = price_able
            return max_val
        return

    else:
        for i in range(len(price) - 1):
            for j in range(i + 1, len(price)):
                price[i], price[j] = price[j], price[i]
                if (int(''.join(price)), cnt) not in visited:
                    visited.add((int(''.join(price)), cnt))
                    back(cnt + 1, change)
                price[i], price[j] = price[j], price[i]


for tc in range(1, int(input()) + 1):
    num, change = map(int, input().split())

    price = []
    for n in str(num):
        price.append(n)

    max_val = 0

    visited = set()

    back(0, change)

    print(f'#{tc} {max_val}')