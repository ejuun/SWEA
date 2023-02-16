T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pc = list(map(int, input().split()))

    def win(start, end):
        if start == end:
            return start
        elif start == 1 and end == 3: #가위, 보
            return start
        elif start == 2 and end == 1: #바위, 가위
            return start
        elif start == 3 and end == 2: #보, 바위
            return start
        else:
            return end

    def winner(start, end):
        if start == end:
            return pc[start]
        else:
            mid = (start + end) // 2
            a = winner(start, mid)
            b = winner(mid + 1, end)
            return win(a, b)

    w = winner(0, N-1)
    print(f'#{tc} {pc.index(w)+1}')
