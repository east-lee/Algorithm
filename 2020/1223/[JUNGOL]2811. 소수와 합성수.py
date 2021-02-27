import math

for _ in range(10):
    arr = list(map(int,input().split()))
    for num in arr:
        x = int(math.sqrt(num))+1
        cnt = 0
        for i in range(1,x):
            if num % i == 0:
                cnt += 1
            if cnt == 2:
                break
        if cnt == 1 and num == 1:
            print('number one')
        elif cnt == 1:
            print('prime number')
        else:
            print('composite number')