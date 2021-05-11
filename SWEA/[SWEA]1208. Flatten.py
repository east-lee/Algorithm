T = 10
for t in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    result = 0
    cnt = 0
    while cnt < n:
        max_num = max(arr)
        min_num = min(arr)
        max_idx = arr.index(max_num)
        min_idx = arr.index(min_num)
        if max_num == min_num or max_num == min_num +1:
            result = max_num -min_num
            break
        arr[min_idx] +=1
        arr[max_idx] -=1
        cnt +=1
    max_num = max(arr)
    min_num = min(arr)
    result = max_num - min_num
    print(f'#{t} {result}')
