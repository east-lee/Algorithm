import math

T = int(input())
for t in range(1,T+1):
    n = int(input())
    result = 0
    for _ in range(n):
        x,y = map(int,input().split())
        r = math.sqrt(x**2+y**2)
        if r <= 200:            
            for i in range(10):
                if i*20<r<=(i+1)*20:
                    result += i
                    break
    print(f'#{t} {result}')
