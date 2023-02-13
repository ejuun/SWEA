T = int(input())
for tc in range(1, T+1):
    word = input()
    top = -1
    stack = [0] * len(word)

    def push(item):
        global top
        top += 1
        stack[top] = item

    def pop():
        global top
        stack[top] = 0
        top -= 1

    for alpha in word:
        if alpha not in stack:
            push(alpha)
        else:
            if stack[top] == alpha:
                pop()
            else:
                push(alpha)

    cnt = 0
    for not_zero in stack:
        if not_zero != 0:
            cnt += 1
    print(f'#{tc} {cnt}')