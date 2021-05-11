import math
for _ in range(10):
    n, m = map(int,input().split())
    result =0
    for i in range(n,m+1):
        print(i)
        if i == n:
            continue
        prime = 1
        for j in range(2,int(math.sqrt(i))):
            if i%j == 0:
                prime = 0
                break
        if prime:
            result +=1
    print(result)