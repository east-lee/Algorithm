import math
for _ in range(10):
    n = int(input())
    n_check = math.sqrt(n)
    result = []
    for i in range(1,int(n_check)+1):
        if n%i==0:
            print(i,end = ' ')
            result.append(i)
    result = result[::-1]
    for i in result:
        if n // i == i:
            continue
        else:
            print(n//i,end=' ')
    print()
