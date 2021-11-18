def solution(n):
  global arr
  arr.pop() if n==0 else arr.append(n)

if __name__ == "__main__":
  K = int(input())
  arr = []
  for _ in range(K):
    n = int(input())
    solution(n)


  print(sum(arr))