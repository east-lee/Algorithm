def main(k,n,last_result,result):
  global result_cnt
  if k == n:
    if last_result ==result:
      result_cnt += 1
    return
  elif result > 20 or result < 0:
    return
  main(k+1,n,last_result,result+arr[k])
  main(k+1,n,last_result,result-arr[k])





if __name__ == "__main__":
  N = int(input())
  arr = list(map(int,input().split()))
  result_cnt = 0
  main(1,len(arr)-1,arr[-1],arr[0])
  print(result_cnt)