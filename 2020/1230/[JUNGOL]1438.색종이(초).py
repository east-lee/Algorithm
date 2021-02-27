testing = True
while testing:
    n = int(input())
    if not n:
        break
    max_x = 0
    max_y = 0
    check = []
    for _ in range(n):
        left_dis, right_dis = map(int,input().split())
        check.append([left_dis,right_dis])
        if left_dis+10 > max_x:
            max_x = left_dis+10
        if right_dis+10>max_y:
            max_y = right_dis+10
    arr = list([0]*max_x for _ in range(max_y))
    for i in check:
        left_dis,right_dis = i[0],i[1]
        for i in range(right_dis,right_dis+10):
            for j in range(left_dis,left_dis+10):
                if not arr[i][j]:
                     arr[i][j] = 1
    result = 0
    for i in range(max_y):
        for j in range(max_x):
            if arr[i][j] == 1:
                result += 1
    print(result)

