def main():
  global result
  if x in S:
    print(0)
    return

  start, end = 0,0
  for i in S:
    if i < x: start = i
    if i>x and not end:
      end = i
      break
  solution(end-start-1,start,end)

def solution(n,start,end):
  if n<2:
    print(0)
    return
  total_cnt = factorial(n)/(factorial(2)*factorial(n-2))

  only_left = x-start-1
  only_right = end-x-1

  if only_left >= 2:
    total_cnt -= factorial(only_left)/(factorial(2)*factorial(only_left-2))
  if only_right >=2:
    total_cnt -= factorial(only_right) / (factorial(2) * factorial(only_right - 2))
  print(int(total_cnt))

def factorial(n):
  return n*factorial(n-1) if n>1 else 1




if __name__ == "__main__":
  L = int(input())
  S = list(map(int,input().split()))
  x = int(input())
  result = 0
  main()
