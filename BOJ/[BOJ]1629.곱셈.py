def get_data():
  A, B, C = map(int, input().split())
  return [A, B, C]

def solution(num_a, num_b):
  if num_b == 1:
    return num_a % C

  num = solution(num_a, num_b//2)

  if num_b % 2 == 0:
    return num*num%C
  else:
    return num*num*num_a%C

if __name__ == "__main__":
  A, B, C = get_data()
  print(solution(A, B))