for tc in range(1, 11):
    length, number = map(str, input().split())

    top = -1
    stack = [0] * len(number)

    def push(item):
        global top
        top += 1
        stack[top] = item

    def pop():
        global top
        stack[top] = 0
        top -= 1

    for num in number:
        if num not in stack:
            push(num)
        else:
            if stack[top] == num:
                pop()
            else:
                push(num)

    ans = ''
    for word in stack:
        if word == 0 :
            break
        else:
            ans += word

    print(f'#{tc} {ans}')