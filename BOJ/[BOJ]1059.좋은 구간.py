def main():
  global S
  result = 0
  S.sort()
  left_num,right_num = [1,max(S)+1]

  for s in S:
    if s < n: left_num = s + 1
    elif s > n :
      right_num = s -1
      break

  while left_num <= n:
    if n == left_num:
      result += (right_num - n)
    elif n > left_num:
      result += (1 + (right_num-n))
    left_num+=1
    
  print(result)

if __name__ == "__main__":
  L = int(input())
  S = list(map(int,input().split()))
  n = int(input())
  if n in S:
    print(0)
  else:
    main()