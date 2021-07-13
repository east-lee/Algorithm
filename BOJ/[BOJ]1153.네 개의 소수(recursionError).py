def find_result(k=0,result='',sum_result=0,last_idx=0):
  global mid_result, final_result

  if mid_result: return

  if k == 3 and N-sum_result > 0:
    if check_num[N-sum_result] == False:
      mid_result = True
      result += str(N-sum_result) + ' '
      final_result = result
      return
    else:
      return

  if sum_result >= N or k == 4 or last_idx == len(prime):
    return

  for i in range(last_idx,len(prime)):

    find_result(k+1,result + str(prime[i]) + ' ',sum_result+prime[i],i)
    find_result(k,result,sum_result,i+1)


def get_prime():
  check_num = [False] * (N+1)
  check_num[0], check_num[1] = [True for _ in range(2)]
  prime = []
  for x in range(2,N+1):
    if check_num[x] == False:
      num = x * 2
      prime.append(x)
      while num <= N:
        check_num[num] = True
        num += x
  return [check_num,prime]


if __name__ == "__main__":
  N = int(input())
  check_num, prime = get_prime()
  mid_result = False
  final_result = -1
  print(len(prime))
  find_result()
  print(final_result)