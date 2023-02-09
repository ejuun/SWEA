T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())

    cnt = 0

    while len(A) >= 1:
        i = 0
        if len(A) >= len(B) and A[i:i+len(B)] == B:
            A = A.replace(B,'',1)
            cnt += 1
        else:
            A = A.replace(A[i], '', 1)
            cnt += 1

    print(f'#{tc} {cnt}')
