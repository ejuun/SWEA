def find_set(x):  # x가 속한 집합의 대표 원소를 구하는 함수
    # 자기 자신이 대표가 될때까지 반복
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):  # y의 대표 원소가 x를 가리키도록 설정
    # disjoint한 두 트리 연결
    p[find_set(y)] = find_set(x)


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    p = [i for i in range(V + 1)]
    G = []

    for _ in range(E):
        u, v, weight = map(int, input().split())
        G.append([u, v, weight])

    G.sort(key=lambda x: x[2])

    s = 0  # MST에 포함된 간선의 가중치의 합
    cnt = 0

    for v, u, w in G:
        if find_set(u) != find_set(v):  # 사이클이 생기지 않는다면
            # 서로 다른 트리라면
            cnt += 1
            s += w  # 가중치 합
            union(v, u)
            if cnt == V:  # MST 구성 완료
                break

    print(f'#{tc} {s}')