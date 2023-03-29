# def quick(s, e):
#     if s >= e:
#         return
#     pivot = s
#
#     i, j = s, e
#
#     while i <= j:
#         while i <= e and arr[pivot] >= arr[i]:
#             i += 1
#         while arr[pivot] < arr[j]:
#             j -= 1
#
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[s], arr[j] = arr[j], arr[s]
#     quick(s, j - 1)
#     quick(j + 1, e)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = quick_sort(arr)
    print(f'#{tc} {ans[N // 2]}')

