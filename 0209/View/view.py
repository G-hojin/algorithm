import sys
sys.stdin = open('input.txt')

T = 10
for i in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    view = 0

    for dex_1 in range(2, N-2):
        if buildings[dex_1] > buildings[dex_1-2] and buildings[dex_1] > buildings[dex_1-1] and buildings[dex_1] > buildings[dex_1+1] and buildings[dex_1] > buildings[dex_1+2]:
            max_height = buildings[dex_1 - 2]
            for dex_2 in range(-2, 3):
                if dex_2 == 0:
                    continue
                if buildings[dex_1 - dex_2] > max_height:
                    max_height = buildings[dex_1 - dex_2]
            view += buildings[dex_1] - max_height

    # for k in range(2, N-2):
    #     # 현재위치와 좌우 2칸씩의 차의 최소값
    #     min_value = 987654321
    #     for a in range(5):
    #         if a != 2:
    #             if buildings[k] - buildings[k-2+a] < min_value:
    #                 min_value = buildings[k] - buildings[k-2+a]
    #     if min_value > 0:
    #         view += min_value

    print(f"#{i} {view}")

