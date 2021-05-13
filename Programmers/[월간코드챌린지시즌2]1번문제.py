def solution(left, right):
  answer = 0
  check = [0] * (right + 1)

  for i in range(1, right + 1):
    x = i
    while x <= right:
      check[x] += 1
      x += i

  for i in range(left, right + 1):
    if check[i] % 2: answer -= i
    else: answer += i
    
  return answer