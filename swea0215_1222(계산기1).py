for tc in range(1, 11):
    length = int(input())
    infix = map(str, input())

    stack = []
    postfix = ''
    top = -1

    for token in infix:
        if token == '+':
            stack.append(token)
        else:
            postfix += token

    while stack:
        postfix += stack.pop()

    for token in postfix:
        if token == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        else:
            stack.append(int(token))

    print(f'#{tc} {stack[0]}')
