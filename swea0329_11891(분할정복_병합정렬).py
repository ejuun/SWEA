def merge(s,e):
    global cnt

    if s == e:
        return
    mid = (s+e-1)//2
    merge(s, mid)
    merge(mid+1, e)

    if arr[mid] > arr[e]:
        cnt += 1

    i, j, k = s, mid+1, s

    while i <= mid and j <= e:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            temp[k] = arr[j]
            j, k = j + 1, k + 1

    while i <= mid:
        temp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= e:
        temp[k] = arr[j]
        j, k = j + 1, k + 1

    for l in range(s, e+1):
        arr[l] = temp[l]


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    temp = [0] * N
    cnt = 0

    merge(0,N-1)

    print(f'#{tc} {arr[N//2]} {cnt}')