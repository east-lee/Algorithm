if __name__ == "__main__":
  N, K = map(int,input().split())
  num = input()
  k = K
  stack = []

  for i in range(N):
    while stack and k and int(stack[-1])<int(num[i]):
      stack.pop()
      k -= 1
    stack.append(num[i])
  stack = stack[:N-K]
  print(''.join(stack))