# from collections import deque
# for _ in range(10):
#
#     Q = deque()
#     N = int(input())
#     num_list = list(map(int, input().split()))
#
#     for i in num_list:
#         Q.append(i)
#
#     while True:
#         for i in range(1, 6):
#             a = Q.popleft() - i
#             if a <= 0:
#                 a = 0
#             Q.append(a)
#             if a == 0:
#                 break
#
#         if a == 0:
#             break
#
#     print(f'#{N}', end=' ')
#     for i in Q:
#         print(i, end=' ')
#     print()

for _ in range(1):
    N = int(input())
    queue = list(map(int, input().split()))

    front = rear = 0

    def enqueue(item):
        global rear

        rear = (rear + 1) % 8
        queue[rear] = item

    while True:
        if queue[rear] == 0:
            break

        for i in range(1, 6):
            enqueue(queue[rear]-i)
            if queue[rear] <= 0:
                queue[rear] == 0

        print(*queue)