def solution(x):
  if x.count('1') == 1:
    return 1
  return 0

if __name__ == "__main__":

  n = int(input())
  bin_n = bin(n)[2:]

  print(solution(bin_n))