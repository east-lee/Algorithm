n,m = map(int,input().split())
arr = list(list(map(int,input().rstrip())) for _ in range(n))
result = 0

for i in range(n):
  for j in range(m):
    if i>0 and j>0 and arr[i][j] == 1:
      arr[i][j] += min(arr[i-1][j],arr[i][j-1],arr[i-1][j-1])
    result = max(result,arr[i][j])
print(result**2)