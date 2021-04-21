def main():
  n = int(input())
  port_num = list(map(int,input().split()))

  return solution(n,port_num)

def solution(n,port_num):
  result = [1]*n
  for i in range(n):
    max_num = 1
    for j in range(i):
      if port_num[i] > port_num[j] and result[j] >= max_num:
        max_num = result[j]+1
    result[i] = max_num
  # print(result)
  return max(result)

if __name__ == "__main__":
  print(main())