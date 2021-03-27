N = int(input())
arr = list(map(int,input().split()))
DP = list([0]*21 for _ in range(len(arr)))

DP[0][arr[0]] = 1

for i in range(1,len(arr)-1):
  for j in range(21):
    if DP[i-1][j]:
      if 0<=j+arr[i]<=20:
        DP[i][j+arr[i]] += DP[i-1][j]
      if 0<=j-arr[i]<=20:
        DP[i][j-arr[i]] += DP[i-1][j]
print(DP[N-2][arr[N-1]])

# for i in DP:print(i)