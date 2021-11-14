def get_data():
  N = int(input())
  arr = list(map(int,input().split()))

  return [N, arr]

def solution():
  global result

  for i in range(N):
    for j in range(i+1, N):
      result += arr[i] * arr[j]

if __name__ == "__main__":
  N, arr = get_data()
  result = 0

  solution()
  print(result)