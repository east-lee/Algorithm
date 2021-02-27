def f(k,sum_result,result_list):
    global result
    if k==n:
        if sum_result == m:
            result.append(result_list)
        return
    for i in range(1,7):
        rr = result_list[:]
        sum_result += i
        rr.append(i)
        f(k+1, sum_result,rr)
        sum_result -= i


testing= True
while testing:
    input_data = input()
    if not input_data:
        break
    n,m = map(int,input_data.split())
    result = []
    f(0,0,[])
    for i in result:
        for j in i:
            print(j,end=' ')
        print()