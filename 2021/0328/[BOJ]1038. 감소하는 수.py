def main():
  global idx,DP
  total_cnt,length_cnt,result,result_length,result_i,idx = 10,2,0,0,0,0

  while total_cnt <=N:

    for i in range(length_cnt-1,10):
      DP[length_cnt][i] = DP[length_cnt-1][i-1] + DP[length_cnt][i-1]
      if total_cnt + DP[length_cnt][i]> N:
        result = total_cnt
        result_i = i
        result_length = length_cnt
        idx = N-total_cnt
        break
      else:
        total_cnt += DP[length_cnt][i]

    if result: break

    length_cnt += 1

  solution(result_i,result_length-1,idx,str(result_i),0)

def solution(last_i, n, idx, result_str,k):
  global result_list
  if k == n:
    result_list.append(int(result_str))
    return

  for i in range(10):
    if last_i > i:
      solution(i,n,idx,result_str+str(i),k+1)


if __name__ == "__main__":
  N = int(input())
  DP = list([0]*10 for _ in range(100))

  for i in range(10):
    DP[1][i] = 1
  if N <= 9:
    print(N)
  else:
    if N > 1022:
      print(-1)
    else:
      result_list = []
      main()
      result_list.sort()

      print(result_list[idx])