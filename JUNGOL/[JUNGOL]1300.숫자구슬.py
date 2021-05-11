def function(k,last_idx,group_list):
    global min_result,result_group
    if k == m-1:
        max_result=0
        new_group = arr[last_idx:]
        group_list.append(new_group)
        for i in group_list:
            check_sum = sum(i)
            if check_sum > max_result:
                max_result = check_sum
        if max_result < min_result:
            min_result = max_result
            for idx,i in enumerate(group_list):
               result_group[idx] = len(i)
        group_list.pop()
        return

    for i in range(last_idx+1,n-m+k+2):
        start = last_idx
        end = i
        new_group = arr[start:end]
        group_list.append(new_group)
        function(k+1,end,group_list)
        group_list.pop()


testing = True
while testing:
    data = input()
    if not data:
        testing = False
        break

    n,m=map(int,data.split())
    arr = list(map(int,input().split()))
    result_group = [0]*m
    min_result = sum(arr)
    function(0,0,[])
    print(min_result)
    for i in result_group:
        print(i,end=' ')
    print()