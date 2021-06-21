def dfs(n,last_num,k,result):
  global count, print_result

  if k == n-1:
    count += 1
    if count == N:
      print_result = int(result)
    return

  for i in range(10):
    if i >= last_num:
      break
    dfs(n,i,k+1,result+str(i))

if __name__ == "__main__":
  N = int(input())
  count = 0
  print_result = -1
  for num_length in range(1,11):
    for start_num in range(10):
      dfs(num_length,start_num,0, str(start_num))

  print(print_result)