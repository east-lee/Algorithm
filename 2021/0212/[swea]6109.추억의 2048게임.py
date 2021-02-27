direction_str_to_num = {'left':0,'right':1,'up':2,'down':3}
#direction_var > [가로:0 or 세로:0 탐색방식 range(n) or range(n-1,-1,0)]
direction_var = [[0,0],[0,1],[1,0],[1,1]]

T = int(input())
for t in range(1,T+1):
    n, direction = map(str,input().split())
    n, direction = int(n), direction_str_to_num[direction]
    arr = list(list(map(int,input().split())) for _ in range(n))
    check = list([0]*n for _ in range(n))

    dir, range_n = direction_var[direction]

    if range_n: range_n = range(n-1,-1,-1)
    else:range_n = range(n)

    for i in range_n:
        stack = []
        check_plus = False
        for j in range_n:
            if not dir:
                arr_now = arr[i][j]
            else:
                arr_now = arr[j][i]
            if not arr_now:
                continue
            if check_plus or not stack:
                check_plus = False
                stack.append(arr_now)
            elif stack[-1] == arr_now:
                stack[-1] = 2 * stack[-1]
                check_plus = True
            elif stack[-1]!=arr_now:
                stack.append(arr_now)
        if direction ==1 :
            stack = stack[::-1]
            for _ in range(n - len(stack)):
                stack.insert(0,0)
        else:
            for _ in range(n-len(stack)):
                stack.append(0)

        if direction ==0:
            for k in range(n):
                check[i][k] = stack[k]
        elif direction == 1:
            for k in range(n-1,-1,-1):
                check[i][k] = stack[k]

        elif direction ==2 :
            for k in range(n):
                check[k][i] = stack[k]
        else:
            for k in range(n-1,-1,-1):
                check[k][i] = stack[n-k-1]

    print(f'#{t}')
    for i in range(n):
        for j in range(n):
            print(check[i][j],end=' ')
        print()




