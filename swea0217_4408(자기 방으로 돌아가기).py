# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
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