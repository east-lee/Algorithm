n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
dp = [0]*(n+1)
dp[1] = 1

for i in range(2,n+1):
    check_num = arr[2]
    dp_list = []
    for j in range(i):
        if arr[j]<arr[i]:
            dp_list.append(dp[j])
    dp[i] = max(dp_list)+1
print(max(dp))