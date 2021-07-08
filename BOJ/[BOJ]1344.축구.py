def DFS(A_score, B_score,time_section,percentage):
  global result

  if time_section == section_cnt:
    if prime[A_score] or prime[B_score]:
      result += percentage
    return

  # A만너을경우
  # B만너을경우
  # 둘다 너을경우
  # 둘다 안너을경우

  DFS(A_score + 1, B_score, time_section + 1, percentage * A * (1 - B))
  DFS(A_score, B_score + 1, time_section + 1, percentage * (1 - A) * B)
  DFS(A_score + 1, B_score + 1, time_section + 1, percentage * A * B)
  DFS(A_score, B_score, time_section + 1, percentage * (1 - A) * (1 - B))


def get_data():
  A = int(input())
  B = int(input())

  return 0.01 * A, 0.01*B

def get_prime():

  prime = [True] * (section_cnt+1)
  prime[0], prime[1] = False, False

  for i in range(2,section_cnt+1):
    x = i
    if prime[x]:
      x += i
      while x <=section_cnt:
        prime[x] = False
        x += i
  return prime



  return prime

if __name__ == "__main__":
  A, B = get_data()
  section_cnt = 18
  prime = get_prime()
  result = 0

  DFS(0,0,0,1)

  print(result)