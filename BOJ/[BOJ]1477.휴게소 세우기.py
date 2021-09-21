

def get_data():
  N, M, L = map(int, input().split())
  restarea = list(map(int, input().split()))
  restarea.extend([0, L])
  restarea.sort()

  return [N, M, L, restarea]


if __name__ == "__main__":
  N, M, L, restarea = get_data()
  left, right = 0, L
  result = 0

  while left <= right:
    restarea_cnt = 0
    mid = (left+right) // 2

    for i in range(len(restarea)-1):
      if (restarea[i+1] - restarea[i]) > mid:
        restarea_cnt += (restarea[i+1]-restarea[i]-1)//mid

    if restarea_cnt > M: left = mid + 1
    else:
      right = mid-1
      result = mid

  print(result)
