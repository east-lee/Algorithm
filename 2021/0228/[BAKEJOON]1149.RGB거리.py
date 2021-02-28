n = int(input())
dp = []
RGB = []
for _ in range(n):
    RGB.append(list(map(int,input().split())))

dp.append(RGB[0])
for i in range(1,n):
     i_min = [0,0,0]
     i_min[0] = min(dp[i-1][1],dp[i-1][2]) + RGB[i][0]
     i_min[1] = min(dp[i-1][0],dp[i-1][2]) + RGB[i][1]
     i_min[2] = min(dp[i-1][0],dp[i-1][1]) + RGB[i][2]
     dp.append(i_min)
print(min(dp[n-1]))
