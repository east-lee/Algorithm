def solution(i,j,check):
    global result
    if check[i][j]:
        return 0
    if max(arr[i]) != arr[i][j]:
        return 0
    check[i] = [1]*m
    col_list = []
    col_check = False
    for k in range(n):
        col_list.append(arr[k][j])
    if max(col_list) == arr[i][j]:
        col_check = True
        for k in range(n):
            check[k][j] = 1
    if col_check:
        return 1
    else:return 0

T = int(input())
for t in range(1,T+1):
    n,m,q = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(n))
    change = list(list(map(int,input().split())) for _ in range(q))
    result = 0
    cnt =0
    while cnt < q:
        cnt += 1
        x, y, change_arr = change[cnt - 1]
        arr[x - 1][y - 1] = change_arr
        check = list([0]*m for _ in range(n))
        for i in range(n):
            for j in range(m):
                result += solution(i,j,check)
    print(f'#{t} {result}')