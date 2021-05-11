def go(result,k,can_go):
    global min_result,N
    if k==N-1:

        if min_result > result:
            min_result = result
        return
    # 갈수 없다면 무조건 교체
    if not can_go:
        go(result+1, k+1, arr[k]-1)
    # 다음으로 갈 수 있다면 교체하거나 교체 안하는거로
    else:
        # 1. 교체 할 경우
        if result+1 < min_result:
            go(result+1, k+1, arr[k]-1)
        # 2. 교체 안할 경우
        go(result,k+1, can_go-1)

T = int(input())

for t in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr[0]
    arr = arr[1:]
    min_result = N
    go(0,1,arr[0]-1)
    print(f'#{t} {min_result}')