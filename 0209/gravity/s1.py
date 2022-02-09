import sys
sys.stdin=open('input.txt')

T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     boxes = list(map(int, input().split()))
#     print(boxes)

    # print(f'{tc}{arr}')

for tc in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    max_value = 0

    for dex_1 in range(N):
        cnt = 0
        for dex_2 in range(dex_1 + 1, N):
            if boxes[dex_1] > boxes[dex_2]:
                cnt += 1

            if cnt > max_value:
                max_value = cnt

    print(f'#{tc} {max_value}')