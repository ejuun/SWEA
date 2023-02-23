T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    heap = [0] * (N+1) #완전 이진트리이므로 1~ N번까지 인덱스 준비
    last = 0 #마지막 정점 번호
    #삽입
    def enq(n):
        global last

        last += 1 #삽입하니 정점추가
        heap[last] = n #마지막 정점에 값 저장
        c = last #부모가 있고, 부모값 < 자식 값 조건 검사 위해 c(자식)을 마지막 정점으로 설정
        p = c // 2 #부모 == 자식 노드 // 2

        while p > 0 and heap[p] > heap[c]: #부모 존재, 부모 값이 더 크다면
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c // 2

        return

    #삭제
    def deq():
        global last

        tmp = heap[1]
        heap[1] = heap[last]
        last -= 1
        p = 1
        c = p * 2

        while c <= last: #자식이 1명 이상일 때
            if c + 1 <= last and heap[c] > heap[c+1]: #자식이 2개이면서 오른쪽 자식의 값이 더 작으면
                c += 1

            if heap[c] < heap[p]:
                heap[c], heap[p] = heap[p], heap[c]
                p = c
                c = p * 2
            else:
                break

        return tmp

    for i in range(len(num)):
        enq(num[i])

    hap = 0
    while N:
        N = N // 2
        hap += heap[N]

    print(f'#{tc} {hap}')