T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #화덕 크기, 피자 갯수

    pi = list(map(int, input().split()))
    pizza = []
    for i in range(len(pi)):
        pizza.append([pi[i], i + 1])

    front = rear = 0
    queue = [0] * (N + 1)

    def enqueue(item):
        global rear
        rear = (rear+1) % len(queue)
        queue[rear] = item

    def dequeue():
        global front
        front = (front+1) % len(queue)
        return queue[front]

    def isEmpty():
        return front == rear

    def isFull():
        return (rear+1) % len(queue) == front

    for i in range(M):
        if isFull():
            while True:
                [c, n] = dequeue()
                c = c // 2
                if c == 0:
                    break
                enqueue([c, n])
        enqueue(pizza[i])

    while not isEmpty():
        [c, n] = dequeue()
        result = n
        c = c // 2
        if c:
            enqueue([c, n])
        # print(queue)
    print(f'#{tc} {result}')