for tc in range(1, 11):
    N = int(input())
    infix = input()
    #중위 표기식 => 후위표기식 변환
    icp = {'+': 1, '*':2}
    isp = {'+': 1, '*':2}
    postfix = ''
    stack = []
    top = -1

    for token in infix:
        if token in icp: #연산자이면
            #스택 비어있는지 확인 후 연산자 우선순위 확인
            while stack and icp[token] < isp[stack[-1]]:
                postfix += stack.pop()
            stack.append(token)
        else: #비연산자이면
            postfix += token

    while stack:
        postfix += stack.pop()


    #변환된 후위표기식에서 값 계산
    for token in postfix:
        if token in isp:
            b = stack.pop()
            a = stack.pop()

            if token == '+' : stack.append(a+b)
            elif token == '*' : stack.append(a*b)
        else:
            stack.append(int(token))

    print(f'#{tc} {stack[0]}')