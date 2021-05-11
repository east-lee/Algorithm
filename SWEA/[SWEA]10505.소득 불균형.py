T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    avg_arr = sum(arr)//N
    result = 0
    for i in arr:
        if int(i) <= avg_arr:
            result += 1
    print(f'#{t} {result}')