def greatest_common_factor(X, Y):
  if X % Y == 0:
    return Y
  return greatest_common_factor(Y, X % Y)

def get_data():
  # N = 소시지의 수 / M = 평론가의 수
  N, M = map(int, input().split())

  return [N, M]


if __name__ == "__main__":
  N, M = get_data()

  print(M - greatest_common_factor(N, M))
