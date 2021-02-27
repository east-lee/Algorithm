T = int(input())

for t in range(1,T+1):
    n = int(input())
    arr = list(list(map(int,input().split())) for _ in range(n))
    result = 0
    for x,y in arr:
        r= (x**2+y**2)**0.5
        if r >200: continue
        for i in range(1,11):
            r_score = 20*i
            if 20*(i-1)<=r<=r_score:
                result += 11-i
                break
    print(f'#{t} {result}')

