T = 10
for t in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    result = 0
    for i in range(2,n-2):
        now = arr[i]
        diff_h = 0
        for j in range(-2,3):
            if j != 0 and diff_h < arr[i+j]:
                diff_h = arr[i+j]
        if now-diff_h>0:
            result += (now-diff_h)
    print(f'#{t} {result}')
