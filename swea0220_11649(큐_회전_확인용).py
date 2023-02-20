T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    # print(f'#{tc} {num_list[M%N]}')


    queue = [0] * (M * N)
    front = rear = -1

    def enqueue(item):
        global rear
        rear += 1
        queue[rear] = item

    for i in range(M+1):
        enqueue(num_list[i % N])

    print(f'#{tc} {queue[M]}')


