# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     bus_station_dict = {}
#     route_list = []
#     for N_tc in range(1, N+1):
#         Ai, Bi = map(int, input().split())
#         for i in range(Ai, Bi+1):
#             route_list.append(i)
#     P = int(input())
#     for ci in range(P):
#         Ci = int(input())
#         if Ci not in bus_station_dict:
#             bus_station_dict[Ci] = 0
#
#     for route in route_list:
#         if route in bus_station_dict:
#             bus_station_dict[route] += 1
#
#     count_list = list(bus_station_dict.values())
#     print(f'#{tc}', end=' ')
#     print(*count_list)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_station_list = [0] * 5001
    for N_tc in range(1, N+1):
        Ai, Bi = map(int, input().split())
        for i in range(Ai, Bi+1):
            bus_station_list[i] += 1

    count_list =[]
    P = int(input())
    for ci in range(P):
        Ci = int(input())
        count_list.append(bus_station_list[Ci])

    print(f'#{tc}', end=' ')
    print(*count_list)

