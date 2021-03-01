n = int(input())
arr = list(list(map(int,input().split())) for _ in range(n))
check = [[0]*len(arr[i]) for i in range(n)]
check[0][0] = arr[0][0]
check[1][0] = arr[0][0]+arr[1][0]
check[1][1] = arr[0][0] + arr[1][1]
for i in range(2,n):
    for j in range(len(arr[i])):
        if j == len(arr[i])-1:
            check[i][j] = arr[i][j]+check[i-1][j-1]
        elif j == 0:
            check[i][j] = arr[i][j] + check[i-1][0]
        else:
            check[i][j] = arr[i][j]+ max(check[i-1][j-1],check[i-1][j])
print(max(check[n-1]))
