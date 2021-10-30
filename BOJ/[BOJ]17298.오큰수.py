def get_data():
  N = int(input())
  arr = list(map(int, input().split()))

  return [N, arr]

if __name__ == "__main__":
  N, arr = get_data()
  stack = [0]
  result = [str(-1)] * N
  for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
      result[stack.pop()] = str(arr[i])
    stack.append(i)

  print(" ".join(result))