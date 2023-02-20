T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #화덕 크기, 피자 갯수

    pizza = list(map(int, input().split()))
    num_list = [0] * len(pizza)

    queue = [-1] * (N+1)
    front = rear = 0

    def enqueue(item):
        global rear
        rear = (rear + 1) % len(queue)
        queue[rear] = item

    def dequeue():
        global front
        front = (front+1) % len(queue)
        return queue[front]

    def isFull():
        return (rear+1) % len(queue) == front

    def isEmpty():
        return front == rear

    #한바퀴 돌면서 화덕에 피자 넣기
    for i in range(len(queue)):
        enqueue(pizza[i])
        num_list[i] += 1

    for i in range(len(queue), M):
        while True:
            c = dequeue()
            if c:
                num_list[front+1] = 0
                break
            enqueue(c//2)
        enqueue(pizza[i])
        num_list[i] += 1

    while not isEmpty():
        c = dequeue()
        if c:
            num_list[front + 1] = 0
        print(num_list)


    print(f'#{tc} {num_list.index(1)}')



    print(queue)




