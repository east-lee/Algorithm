import math
T = int(input())

for t in range(1,T+1):
    n = int(input())
    cnt = 0
    result = 0
    while cnt <=n+1:
        a,b = n,cnt
        num = math.factorial(a)//((math.factorial(a-b))*(math.factorial(b)))
        if num % 2 ==0:result+=1
    print(f'#{t} {result}')
    >=
