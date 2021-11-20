def solution(sum_energy):
  global max_energy, W

  if len(W) == 2:
    max_energy = max(max_energy, sum_energy)
    return

  for i in range(1, len(W)-1):
    energy = W[i-1] * W[i+1]
    temp_w = W[i]
    W.pop(i)
    solution(sum_energy + energy)
    W.insert(i, temp_w)



def get_data():
  N = int(input())
  W = list(map(int,input().split()))

  return [N, W]

if __name__ == "__main__":
  N, W = get_data()
  max_energy = 0
  solution(0)

  print(max_energy)