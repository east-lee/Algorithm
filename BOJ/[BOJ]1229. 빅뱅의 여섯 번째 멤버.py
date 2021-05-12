def main():
  global N

  dp = [7]*(N+1)
  dp[0] = 0
  for i in range(1,N+1):
    for num in bigbang[1]:
      if num > i: break
      dp[i] = min(dp[i-num]+1,dp[i])
  print(dp[N])

def find_bigbang_num():
  arr = [0] * (N+1)
  arr_2 = []
  x = 1
  plus_num = 1
  while x <= N:
    arr[x] = 1
    arr_2.append(x)
    plus_num += 4
    x += plus_num
  return [arr,arr_2]


if __name__ == "__main__":
  N = int(input())

  bigbang = find_bigbang_num()
  main()