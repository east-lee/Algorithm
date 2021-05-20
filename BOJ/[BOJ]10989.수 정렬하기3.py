import sys

# if __name__ == "__main__":
#   N = int(sys.stdin.readline())
#   num_count = {}
#
#   for _ in range(N):
#     num = sys.stdin.readline()
#     if num in num_count.keys():
#       num_count[num] += 1
#     else: num_count[num] = 1
#
#   num_count = sorted(num_count.items())
#
#   for value, cnt in num_count:
#     for _ in range(cnt):
#       print(value)
import sys
if __name__ == "__main__":
  N = int(sys.stdin.readline())
  num_count = [0]*(10001)
  for _ in range(N):
    num_count[int(sys.stdin.readline())] += 1

  for i in range(10001):
    if num_count[i]:
      for _ in range(num_count[i]):print(i)

