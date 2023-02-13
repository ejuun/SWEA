T = int(input())
for tc in range(1, T+1):
    N = int(input())

    number = list(map(int, input().split()))

    stack = [0] * N

    top = -1

    def push(item):
        global top
        top += 1
        stack[top] = item

    def pop():
        global top
        stack[top] = 0
        top -= 1

    for num in number:
        if num != 0:
            push(num)
        else:
            pop()

    print(stack)

    total_sum = 0
    for i in range(len(stack)):
        total_sum += stack[i]

    print(f'#{tc} {total_sum}')