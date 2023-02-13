T = int(input())
for tc in range(1, T+1):
    check = input()

    stack = [0] * len(check)
    top = -1

    def push(item):
        global top
        top += 1
        stack[top] = item

    def pop():
        global top
        stack[top] = 0
        top -= 1

    cnt = 1
    for word in check:
        if word == '(':
            push(word)
        elif word == '{':
            push(word)
        elif word == ')':
            if stack[top] == '(':
                pop()
            else:
                cnt = 0
                break
        elif word == '}':
            if stack[top] == '{':
                pop()
            else:
                cnt = 0
                break
    if stack[0] != 0:
        cnt = 0

    print(f'#{tc} {cnt}')

# t = int(input())
# for tc in range(1, 1 + t):
#     result = 0
#     string = input()
#
#     top = -1
#     stack = [0] * 50
#
#     def push(item):
#         global top
#         top += 1
#         stack[top] = item
#
#     def pop():  # 가장 마지막에 저장된 자료 반환
#         global top
#         ret = stack[top]
#         top -= 1
#         return ret
#
#     for i in string:
#         if i == '(':
#             push(i)
#         elif i == ')':
#             if stack[top] == '(':
#                 pop()
#             else:
#                 result += 1
#                 break
#
#         elif i == '{':
#             push(i)
#         elif i == '}':
#             if stack[top] == '{':
#                 pop()
#             else:
#                 result += 1
#                 break
#
#     if top != -1 or result > 0:
#         print(f'#{tc} {0}')
#     elif top == -1 and result == 0:
#         print(f'#{tc} {1}')