import math

for _ in range(10):
    n = int(input())
    for _ in range(n):
        result = []
        x = int(input())
        cnt = 0
        while not result:
            x1, x2 = x-cnt, x+cnt
            arr= []
            if x1 >1:
                arr.append(x1)
            if x2>1: arr.append(x2)
            for i in arr:
                check = 0
                for j in range(2,i):
                    if i%j ==0:
                        check = 1
                        break
                if not check and i not in result:
                    result.append(i)
            cnt +=1
        result.sort()

        for i in result:
            print(i,end=' ')
        print()







