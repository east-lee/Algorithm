import math


for _ in range(10):
    n, m = int(input()), int(input())
    result = []
    for i in range(n,m+1):
        if i == 1:
            continue
        cnt = 0
        x = int(math.sqrt(i))+1
        for j in range(1,x):
            if i%j == 0:
                cnt += 1
            if cnt >=2:
                break
        if cnt == 1:
            result.append(i)


    if not result: print(-1)
    else:
        print(sum(result))
        print(result[0])

