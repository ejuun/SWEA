T = int(input())
for tc in range(1, T+1):
    forth = map(str, input().split())

    stack = []
    top = -1

    def push(item):
        global top
        top += 1
        stack.append(item)

    def pop():
        if len(stack) == 0:
            return 'error'
        global top
        ret = stack.pop(top)
        top -= 1
        return ret

    for word in forth:
        if word == '.':
            #계산이 끝났는데 스택에 2개 이상의 숫자가 남아있다면 오류
            if len(stack) > 1:
                ans = 'error'
                break
            #스택에 남아있는 숫자가 1개라면 그 값 반환
            else:
                ans = stack[top]
            break
        #피연산자 입력시
        if word != '*' and word != '+' and word != '-' and word != '/':
            push(int(word))
        #연산자 입력시
        else:
            s2 = pop()
            s1 = pop()
            #스택에 남아 있는 숫자가 없어 error가 반환되었다면 error 출력
            if s1 == 'error' or s2 == 'error':
                ans = 'error'
                break
            new_word = 0
            if word == '+':
                new_word = s1 + s2
            elif word == '-':
                new_word = s1 - s2
            elif word == '*':
                new_word = s1 * s2
            elif word == '/':
                new_word = s1 // s2
            push(new_word)

    print(f'#{tc} {ans}')