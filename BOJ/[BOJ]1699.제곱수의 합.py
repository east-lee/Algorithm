def main():
  dp = [0]*(N+1)

  for i in range(1,N+1):
    check_list = []
    for j in square_number_list:
      if j > i: break
      check_list.append(dp[i-j]+1)
    dp[i] = min(check_list)
  print(dp[N])

def find_square_number():
  square_number = []
  cnt = 1
  while cnt**2 <= N:
    square_number.append(cnt**2)
    cnt+=1
  return square_number

if __name__ == "__main__":
  N = int(input())
  square_number_list = find_square_number()
  main()