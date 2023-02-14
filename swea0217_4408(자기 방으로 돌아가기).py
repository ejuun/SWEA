T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room =[]
    for _ in range(N):
        present, back = map(int, input().split())
        room.append((present,back))

    time = 1
    for i in range(len(room)-1):
        #두 방이 같은 쪽에 있을 때
        if (room[i][0] %2 ==0 and room[i][1] % 2 == 0) or (room[i][0] %2 !=0 and room[i][1] % 2 != 0):
            if room[i+1][0] in range(room[i][0],room[i][1]+2) or room[i+1][1] in range(room[i][0],room[i][1]+2):
                time += 1
        else:
            if room[i+1][0] in range(room[i][0],room[i][1]+1) or room[i+1][1] in range(room[i][0],room[i][1]+1):
                time += 1
    print(f'#{tc} {time}')