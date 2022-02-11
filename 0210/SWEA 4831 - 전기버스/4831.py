import sys
sys.stdin = open('sample_input.txt')

# T = int(input())
# if 1 <= T <= 50:
#     for tc in range(1, T + 1):
#         K, N, M = map(int, input().split())
#         charge_num = list(map(int, input().split()))
#
#         location = 0
#         bus_stop = 0
#         count = 0
#
#         while location + K < N:
#             if location + K >= charge_num[bus_stop + 2]:
#                 location = charge_num[bus_stop + 2]
#                 count += 1
#                 bus_stop += 3
#                 continue
#
#             elif location + K >= charge_num[bus_stop + 1]:
#                 location = charge_num[bus_stop + 1]
#                 count += 1
#                 bus_stop += 2
#                 continue
#             elif location + K < charge_num[bus_stop]:
#                 count = 0
#                 break
#
#             else:
#                 location = charge_num[bus_stop]
#                 count += 1
#                 bus_stop += 1
#
#         print("#%d %d" % (tc, count))

T = int(input())
if 1 <= T <= 50:
    for tc in range(1, T+1):
        K, N, M = map(int, input().split())
        charge_place = list(map(int, input().split()))

        charge = 0
        location = 0

        while location < N:


            for i in range(location + K, location, -1):
                found_station = 0
                if i in charge_place:
                    location = i
                    charge += 1
                    found_station = 1
                    break

            if location + K >= N:
                print(f'#{tc} {charge}')
                break

            if found_station == 0:
                print(f'#{tc} 0')
                break