# for tc in range(1, 11):
#     N = int(input())
#     #y가 양끝에 위치할 때 인덱스 오류 방지 위해 양 끝에 0 한줄씩 추가
#     m = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
#
#     #도착점(2)의 열 위치
#     end = m[99].index(2)
#
#     x = 99
#     y = end
#     while x != 0: #x가 맨 윗줄에 도착할 때까지
#         #만약 왼쪽에 길이 있다면
#         if m[x][y-1] == 1:
#             #0이 안나올때까지 이동
#             n = 1
#             while m[x][y-n] != 0:
#                 n += 1
#             #한칸 더 간 상태로 종료 되어 하나 되돌아가고 그 값을 y에 저장
#             n -= 1
#             y -= n
#             #위로 한칸 올라간다
#             x -= 1
#         #만약 오른쪽에 길이 있다면
#         elif m[x][y+1] == 1:
#             # 0이 안나올때까지 이동
#             n = 1
#             while m[x][y + n] != 0:
#                 n += 1
#             # 한칸 더 간 상태로 종료 되어 하나 되돌아가고 그 값을 y에 저장
#             n -= 1
#             y += n
#             # 위로 한칸 올라간다
#             x -= 1
#         #만약 둘다 없다면 직진
#         else:
#             x -= 1
#     #왼쪽에 1열 추가해줘서 y-1값
#     print(f'#{tc} {y-1}')
for tc in range(1, 11):
    tc_num = int(input())
    arr =[list(map(int, input().split())) for _ in range(100)]

    r = c = 0
    for i in range(100):
        if arr[99][i] == 2:
            r, c = 99, i
            break
    #출발점까지 가는 반복문
    while r: #출발점에 도착할때까지
        #현재위치 (r,c)에서 이동할 다음 위치
        #arr[r][c] = 0 #방법 1 지나온 길을 0으로 만들어버리기
        #방법 2 while문 사용용
       if c-1 >= 0 and arr[r][c-1] == 1: # 왼쪽 확인
           while c-1 >= 0 and arr[r][c-1] == 1:
              c -= 1
       elif c < 99 and arr[r][c+1] == 1: #오른쪽확인
           while c + 1 < 100 and arr[r][c + 1] == 1:
              c += 1
       r -= 1

    print(c)
    # up, left, right = 0, 1, 2
    # dir = up
    #
    # while r:
    #     if dir != right and c-1 >= 0 and arr[r][c-1]:
    #         c -= 1
    #         dir = left
    #     elif dir != left and c+1 < 100 and arr[r][c+1]:
    #         c += 1
    #         dir = right
    #     else:
    #         r -= 1
    #         dir = up
    #
    # print(c)