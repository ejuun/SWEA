T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    A = list(range(1, 13))
    l = len(A)
    cnt = 0
    arr= []
    def find(start):
        global cnt

        if len(arr) == N:
            if sum(arr) == K:
                cnt += 1
            return

        for i in range(start, l):
            if A[i] not in arr:
                arr.append(A[i])
                find(i)
                arr.pop()
    # def find(start, hap, length):
    #     global cnt
    #
    #     if hap > K:
    #         return
    #
    #     if start == l:
    #         if hap == K and length == N:
    #             cnt += 1
    #         return
    #
    #     find(start+1, hap+A[start], length+1)
    #     find(start+1, hap, length)
    # find(0,0,0)
    find(0)

    print(f'#{tc} {cnt}')


