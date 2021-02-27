def f(k,arr1_list,arr2_list,idx_list):
    global result_cnt, result_list
    if k==n:
        arr1_list.sort()
        arr2_list.sort()
        arr1_list = list(set(arr1_list))
        arr2_list = list(set(arr2_list))
        if arr1_list == arr2_list and result_cnt < len(arr1_list):
            result_cnt = len(arr1_list)
            result_list = arr1_list
        return
    r1 = arr1_list[:]
    r2 = arr2_list[:]
    r1.append(arr1[k])
    r2.append(arr2[k])
    idx_list.append(k)
    f(k+1,r1,r2,idx_list)
    idx_list.pop()
    f(k + 1, arr1_list, arr2_list,idx_list)



testing = True
while testing:
    n = int(input())
    if not n: break
    arr1 = [i for i in range(1,n+1)]
    arr2=[0]*n
    for i in range(n):
        arr2[i]= int(input())
    result_list = []
    result_cnt = 0
    f(0,[],[],[])
    print(result_cnt)
    for i in result_list:
        print(i)


