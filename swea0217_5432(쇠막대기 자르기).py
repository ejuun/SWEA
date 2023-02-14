T = int(input())
for tc in range(1, T+1):
    laser = list(map(str, input()))

    stack = []
    top = -1

    def push(item):
        global top
        top += 1
        stack.append(item)

    def pop():
        global top
        stack.pop()
        top -= 1

    cnt = 0
    for i in range(len(laser)):
        if laser[i] == '(':
            push(laser[i])
        elif laser[i-1] == '(' and laser[i] == ')':
            pop()
            cnt += len(stack)
        else:
            pop()
            cnt += +1
    print(f'#{tc} {cnt}')

# T = int(input())
# for tc in range(1, T+1):
#     laser = list(map(str, input()))
#
#     for i in range(len(laser)-1):
#         if laser[i] == '(' and laser[i+1] == ')':
#             laser[i] = 'r'
#             laser[i+1] = ''
#
#     cnt = 0
#     for i in range(len(laser)):
#         if laser[i] == ')':
#         #'(' 가 나올때 까지 j 줄여가면서 검색
#             j = i - 1
#             r = 0
#             while laser[j] != '(':
#                 # 줄이는중 레이저 나오면 레이저 갯수 카운트하기
#                 if laser[j] == 'r':
#                     r += 1
#                 j -= 1
#             # 다른 것과 안겹치게 하기 위해 쌍이된 괄호 0으로 만들어주기
#             laser[i] = 0
#             laser[j] = 0
#             # 막대기 갯수 = 레이저 갯수 + 1
#             cnt += (r + 1)
#     print(f'#{tc} {cnt}')
