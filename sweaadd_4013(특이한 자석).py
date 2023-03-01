from collections import deque
for tc in range(1, int(input()) + 1):
    K = int(input())
    m1 = deque(map(int, input().split()))
    m2 = deque(map(int, input().split()))
    m3 = deque(map(int, input().split()))
    m4 = deque(map(int, input().split()))

    result = 0

    for _ in range(K):
        n, dir = map(int, input().split())

        if dir == 1:
            if n == 1:
                if m1[2] != m2[6]:
                    if m2[2] != m3[6]:
                        if m3[2] != m4[6]:
                            a = m1.pop()
                            m1.insert(0, a)
                            b = m2.popleft()
                            m2.append(b)
                            c = m3.pop()
                            m3.insert(0, c)
                            d = m4.popleft()
                            m4.append(d)
                        else:
                            a = m1.pop()
                            m1.insert(0, a)
                            b = m2.popleft()
                            m2.append(b)
                            c = m3.pop()
                            m3.insert(0, c)
                    else:
                        a = m1.pop()
                        m1.insert(0, a)
                        b = m2.popleft()
                        m2.append(b)
                else:
                    a = m1.pop()
                    m1.insert(0, a)

            elif n == 2:
                if m2[6] != m1[2]:
                    if m2[2] != m3[6]:
                        if m3[2] != m4[6]:
                            b = m2.pop()
                            m2.insert(0, b)
                            a = m1.popleft()
                            m1.append(a)
                            c = m3.popleft()
                            m3.append(c)
                            d = m4.pop()
                            m4.insert(0, d)
                        else:
                            b = m2.pop()
                            m2.insert(0, b)
                            a = m1.popleft()
                            m1.append(a)
                            c = m3.popleft()
                            m3.append(c)
                    else:
                        b = m2.pop()
                        m2.insert(0, b)
                        a = m1.popleft()
                        m1.append(a)

                elif m2[6] == m1[2]:
                    if m2[2] != m3[6]:
                        if m3[2] != m4[6]:
                            b = m2.pop()
                            m2.insert(0, b)
                            c = m3.popleft()
                            m3.append(c)
                            d = m4.pop()
                            m4.insert(0, d)
                        else:
                            b = m2.pop()
                            m2.insert(0, b)
                            c = m3.popleft()
                            m3.append(c)
                    else:
                        b = m2.pop()
                        m2.insert(0, b)

            elif n == 3:
                if m3[2] != m4[6]:
                    if m3[6] != m2[2]:
                        if m2[6] != m1[2]:
                            c = m3.pop()
                            m3.insert(0, c)
                            d = m4.popleft()
                            m4.append(d)
                            b = m2.popleft()
                            m2.append(b)
                            a = m1.pop()
                            m1.insert(0, a)
                        else:
                            c = m3.pop()
                            m3.insert(0, c)
                            d = m4.popleft()
                            m4.append(d)
                            b = m2.popleft()
                            m2.append(b)
                    else:
                        c = m3.pop()
                        m3.insert(0, c)
                        d = m4.popleft()
                        m4.append(d)

                elif m3[2] == m4[6]:
                    if m3[6] != m2[2]:
                        if m2[6] != m1[2]:
                            c = m3.pop()
                            m3.insert(0, c)
                            b = m2.popleft()
                            m2.append(b)
                            a = m1.pop()
                            m1.insert(0, a)
                        else:
                            c = m3.pop()
                            m3.insert(0, c)
                            b = m2.popleft()
                            m2.append(b)
                    else:
                        c = m3.pop()
                        m3.insert(0, c)

            elif n == 4:
                if m4[6] != m3[2]:
                    if m3[6] != m2[2]:
                        if m2[6] != m1[2]:
                            d = m4.pop()
                            m4.insert(0, d)
                            c = m3.popleft()
                            m3.append(c)
                            b = m2.pop()
                            m2.insert(0, b)
                            a = m1.popleft()
                            m1.append(a)
                        else:
                            d = m4.pop()
                            m4.insert(0, d)
                            c = m3.popleft()
                            m3.append(c)
                            b = m2.pop()
                            m2.insert(0, b)
                    else:
                        d = m4.pop()
                        m4.insert(0, d)
                        c = m3.popleft()
                        m3.append(c)
                else:
                    d = m4.pop()
                    m4.insert(0, d)
        else:
            if n == 1:
                if m1[2] != m2[6]:
                    if m2[2] != m3[6]:
                        if m3[2] != m4[6]:
                            a = m1.popleft()
                            m1.append(a)
                            b = m2.pop()
                            m2.insert(0, b)
                            c = m3.popleft()
                            m3.append(c)
                            d = m4.pop()
                            m4.insert(0, d)
                        else:
                            a = m1.popleft()
                            m1.append(a)
                            b = m2.pop()
                            m2.insert(0, b)
                            c = m3.popleft()
                            m3.append(c)
                    else:
                        a = m1.popleft()
                        m1.append(a)
                        b = m2.pop()
                        m2.insert(0, b)
                else:
                    a = m1.popleft()
                    m1.append(a)

            elif n == 2:
                if m2[6] != m1[2]:
                    if m2[2] != m3[6]:
                        if m3[2] != m4[6]:
                            b = m2.popleft()
                            m2.append(b)
                            a = m1.pop()
                            m1.insert(0, a)
                            c = m3.pop()
                            m3.insert(0, c)
                            d = m4.popleft()
                            m4.append(d)
                        else:
                            b = m2.popleft()
                            m2.append(b)
                            a = m1.pop()
                            m1.insert(0, a)
                            c = m3.pop()
                            m3.insert(0, c)
                    else:
                        b = m2.popleft()
                        m2.append(b)
                        a = m1.pop()
                        m1.insert(0, a)

                elif m2[6] == m1[2]:
                    if m2[2] != m3[6]:
                        if m3[2] != m4[6]:
                            b = m2.popleft()
                            m2.append(b)
                            c = m3.pop()
                            m3.insert(0, c)
                            d = m4.popleft()
                            m4.append(d)
                        else:
                            b = m2.popleft()
                            m2.append(b)
                            c = m3.pop()
                            m3.insert(0, c)
                    else:
                        b = m2.popleft()
                        m2.append(b)
            elif n == 3:
                if m3[2] != m4[6]:
                    if m3[6] != m2[2]:
                        if m2[6] != m1[2]:
                            c = m3.popleft()
                            m3.append(c)
                            d = m4.pop()
                            m4.insert(0, d)
                            b = m2.pop()
                            m2.insert(0, b)
                            a = m1.popleft()
                            m1.append(a)
                        else:
                            c = m3.popleft()
                            m3.append(c)
                            d = m4.pop()
                            m4.insert(0, d)
                            b = m2.pop()
                            m2.insert(0, b)
                    else:
                        c = m3.popleft()
                        m3.append(c)
                        d = m4.pop()
                        m4.insert(0, d)

                elif m3[2] == m4[6]:
                    if m3[6] != m2[2]:
                        if m2[6] != m1[2]:
                            c = m3.popleft()
                            m3.append(c)
                            b = m2.pop()
                            m2.insert(0, b)
                            a = m1.popleft()
                            m1.append(a)
                        else:
                            c = m3.popleft()
                            m3.append(c)
                            b = m2.pop()
                            m2.insert(0, b)
                    else:
                        c = m3.popleft()
                        m3.append(c)
            elif n == 4:
                if m4[6] != m3[2]:
                    if m3[6] != m2[2]:
                        if m2[6] != m1[2]:
                            d = m4.popleft()
                            m4.append(d)
                            c = m3.pop()
                            m3.insert(0, c)
                            b = m2.popleft()
                            m2.append(b)
                            a = m1.pop()
                            m1.insert(0, a)
                        else:
                            d = m4.popleft()
                            m4.append(d)
                            c = m3.pop()
                            m3.insert(0, c)
                            b = m2.popleft()
                            m2.append(b)
                    else:
                        d = m4.popleft()
                        m4.append(d)
                        c = m3.pop()
                        m3.insert(0, c)
                else:
                    d = m4.popleft()
                    m4.append(d)

    if m1[0] == 1:
        result += 1
    if m2[0] == 1:
        result += 2
    if m3[0] == 1:
        result += 4
    if m4[0] == 1:
        result += 8

    print(f'#{tc} {result}')