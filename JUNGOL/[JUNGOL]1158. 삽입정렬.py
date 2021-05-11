for _ in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        result = []
        num = i+1
        first_arr = arr[:num]
        second_arr = arr[num:]
        first_arr.sort()
        for k in first_arr:
            result.append(k)
        for j in second_arr:
            result.append(j)
        if i!=0:
            for i in result:
                print(i,end=' ')
            print()




