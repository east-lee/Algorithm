def solution(k,result,last_idx):
  global global_result

  if k == 3:
    if last_idx == -1:
      return

    if result % 2 == 1 and global_result% 2 == 1 and global_result < result: global_result = result
    elif result % 2 == 1 and global_result % 2 == 0: global_result = result
    elif result % 2 == 0 and global_result % 2 == 0 and result > global_result: global_result=result
    elif result % 2 == 0 and global_result == 1:global_result=result
    return

  for i in range(3):
    if last_idx < i:
      solution(k+1,result*arr[i],i)
      solution(k+1,result,last_idx)





arr = list(map(int,input().split()))
global_result = 0
solution(0,1,-1)

print(global_result)
