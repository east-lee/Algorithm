def main():
  end_point = 11
  cnt = 0
  for i in range(1,end_point):
    for j in range(10):
      now_cnt = cnt + dp[i][j]
      if cnt < N <= now_cnt:
        return [i,j,now_cnt-cnt]
      cnt = now_cnt
  return False

def make_dp():
  end_point = 11

  dp = list([0]*10 for _ in range(end_point))

  for i in range(10): dp[1][i] = 1

  for i in range(2,end_point):
    for j in range(10):
      if i-1 > j: dp[i][j] = 0
      else:
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

  return dp

def check(num):
  num = str(num)

  for i in range(1,len(num)):
    if num[i] >= num[i-1]: return 0
  return 1



def find_num(i,j,cnt):
  start_num = int(str(j) + '0'*(i-1))
  end_num  = int(str(j+1) + '0'*(i-1))
  count = 0

  for num in range(start_num,end_num):
    count += check(num)
    if count == cnt:
      return num

def get_N():
  N = int(input())
  return N

if __name__ == "__main__":
  N = get_N()
  dp = make_dp()
  hint_list = main()

  if not hint_list: print('-1')
  else:
    i,j,cnt = hint_list
    print(find_num(i,j,cnt))



