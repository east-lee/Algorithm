import sys
if __name__ == "__main__":
  N = int(sys.stdin.readline())
  arr = [0] * 10001
  for _ in range(N):
    idx = int(sys.stdin.readline())
    arr[idx] += 1

  for i in range(10001):
    if not arr[i]:continue
    for j in range(arr[i]):
      print(i)
