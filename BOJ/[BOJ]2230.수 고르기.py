# 정렬 및 두 포인터


def main():
  left, right = 0, 0

  result = arr[-1] - arr[0] + 1

  while left < N and right < N:
    leftNum, rightNum = arr[left], arr[right]
    diffNum = rightNum - leftNum

    if diffNum == M:
      return M
    elif diffNum > M:
      left += 1
    else: right += 1

    result = min(result, diffNum) if diffNum > M else result

  return result


def get_data():
  N, M = map(int,input().split())
  arr = []

  for _ in range(N):
    inputNum = int(input())
    arr.append(inputNum)

  arr.sort()

  return [N, M, arr]


if __name__ == "__main__":
  N, M, arr = get_data()

  result = main()
  print(result)