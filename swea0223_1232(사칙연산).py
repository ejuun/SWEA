for tc in range(1, 11):

    n = int(input())

    P = [0] * (n+1)
    L = [0] * (n+1)
    R = [0] * (n+1)

    for i in range(n):

        arr = list(map(str, input().split()))

        if arr[1].isdigit():
            P[int(arr[0])] = int(arr[1])

        else:
            P[int(arr[0])] = arr[1]

        if len(arr) == 3:
            L[int(arr[0])] = int(arr[2])

        elif len(arr) == 4:
            L[int(arr[0])] = int(arr[2])
            R[int(arr[0])] = int(arr[3])

    def inorder(v):
        if not v:
            return 0

        a = P[v]
        b = inorder(L[v])
        c = inorder(R[v])

        if not b or not c:
            return a

        if a.isdigit():
            return a

        else:
            if a == '-':
                return b-c

            elif a == '+':
                return b+c

            elif a == '*':
                return b*c

            elif a == '/':
                return b/c

    print(f'#{tc} {int(inorder(1))}')