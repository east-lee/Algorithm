#DP Problem
# 계단은 한번에 한계단 또는 두계단씩 오를 수 있음
# 연속된 세개의 계단을 모두 밟을 수 없음
# 마지막 도착 계단은 반드시 밟아야 함

n = int(input())
arr = list(int(input()) for _ in range(n))
dp = [0]*(n+1)
arr.insert(0,0)
dp[1] = arr[1]
dp[2] = arr[1]+arr[2]
dp[3] = max(arr[1]+arr[3], arr[2]+arr[3])

for i in range(4,n+1):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
print(dp[n])