# T = int(input())
# for tc in range(1, T+1):
#     N = input()
#     M = input()
#
#     if N in M:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')

# T = int(input())
# for tc in range(1, T+1):
#     N = input()
#     M = input()
#
#     cnt = 0
#     length = len(N)
#     for i in range(len(M)-length+1):
#         if M[i:i+length] == N:
#             cnt = 1
#             break
#     print(f'#{tc} {cnt}')

T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()

    n = len(t)
    m = len(p)
    #모든 패턴이 있을 수 있는 시작위치
    for i in range(0, n-m+1):
        #t[i:i+m]
        # found = True  #플래그(flag) 변수
        for j in range(m):
            if p[j] != t[i+j]:
                # found = False
                break
        else:
            pass
            #잡았다 요놈...

        # if found:
        #     print(i, t[i:i + m])
