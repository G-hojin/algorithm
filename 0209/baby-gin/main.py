import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input()))
    arr = [0] * 10

    for dex in num:
        arr[dex] += 1

    i = 0
    run = 0
    triplet = 0

    while i < 10:
        if arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
            run += 1
            continue

        if arr[i] >= 3:
            arr[i] -= 3
            triplet += 1
            i -= 1
            continue
        i += 1

    if run + triplet >= 2:
        print(f'#{tc} 1')

    else:
        print(f'#{tc} 0')
