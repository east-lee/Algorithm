def f(k,result_list):
    if result_list and len(result_list)==6 or k==n:
        if len(result_list) == 6:
            for i in result_list:
                print(i,end=' ')
            print()
        return
    r = result_list[:]
    rr = result_list[:]
    r.append(arr[k])
    
    f(k+1,r)
    f(k+1,rr)


testing = True
while testing:
    data_input = input()
    if not data_input: break
    arr = list(map(int,data_input.split()))
    n = arr[0]
    arr = arr[1:]
    arr.sort()
    f(0,[])