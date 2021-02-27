T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = 1
    min_num = min(arr)
    max_num = max(arr)

    num=0
    if arr[0]==min_num and arr[-1]==max_num:
        result = 1
    else:
        for i in arr:
            if i > num:
                num = i
                continue
            else:
                result += 1
            num = i

    print(f'#{t} {result}')
