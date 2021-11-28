def get_data():
  N = int(input())
  arr = []

  for _ in range(N):
    data_list = list(map(str, input().split()))
    for i in range(1,4):
      data_list[i] = int(data_list[i])
    arr.append(data_list)

  return [N, arr]

def solution_sorting():
  global arr

  arr.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

if __name__ == "__main__":
  N, arr = get_data()
  solution_sorting()

  for name, score_a, score_b, score_c in arr:
    print(name)

