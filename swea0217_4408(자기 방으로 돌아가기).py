# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
<<<<<<< HEAD
    # room =[]
    # for _ in range(N):
    #     present, back = map(int, input().split())
    #     room.append((present,back))
    #
    # time = 1
    # for i in range(len(room)-1):
    #     #두 방이 같은 쪽에 있을 때
    #     if (room[i][0] %2 ==0 and room[i][1] % 2 == 0) or (room[i][0] %2 !=0 and room[i][1] % 2 != 0):
    #         if room[i+1][0] in range(room[i][0],room[i][1]+2) or room[i+1][1] in range(room[i][0],room[i][1]+2):
    #             time += 1
    #     else:
    #         if room[i+1][0] in range(room[i][0],room[i][1]+1) or room[i+1][1] in range(room[i][0],room[i][1]+1):
    #             time += 1
    # print(f'#{tc} {time}')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     room = [0] * 200
#     for _ in range(N):
#         start, end = map(int, input().split())
#         #방 번호가 바뀌면 밑에 오류 발생
#         if start > end:
#             start, end = end, start
#         # (방 번호 -1) // 2 의 몫이 같은 방은 복도를 공유하는 사이이기 때문 ex) 1-3, 4-6번을 갔을 때 걸리는 이동시간은 2초
#         #이를 고려
#         for i in range((start-1)//2, (end-1)//2 + 1):
#             room[i] += 1
#
#     print(f'#{tc} {max(room)}')
#     room =[0] * 500
#     for _ in range(N):
#         present, back = map(int, input().split())
#         if present > back:
#             present, back = back, present
#
#         for i in range(present, back+1):
#             room[i] += 1
#
#     print(f'#{tc} {max(room)}')

T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    cnts = [0] * 200

    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s

        for i in range((s-1)//2, (e-1)//2 + 1):
            cnts[i] += 1

    ans = max(cnts)

    print(f'#{tc} {ans}')

