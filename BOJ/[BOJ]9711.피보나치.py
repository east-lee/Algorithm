def get_data():
  N = int(input())
  arr =[]
  max_x = -1
  for _ in range(N):
    x, Q = map(int, input().split())
    arr.append([x, Q])
    max_x = max(max_x, x)

  return [N, arr, max_x]

def fibonacci(x, Q):
  fibonacci_arr = [0] * (x+1)
  fibonacci_arr[1] = 1 % Q
  point = 1

  while point < x:
    fibonacci_arr[point + 1] = (fibonacci_arr[point-1] + fibonacci_arr[point]) % Q
    point += 1

  return fibonacci_arr[x]

if __name__ == "__main__":
  N, arr, max_x = get_data()

  for tc in range(N):
    x, Q = arr[tc]
    result = fibonacci(x, Q)
    print(f'Case #{tc+1}: {result}')