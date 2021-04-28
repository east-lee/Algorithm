def main():
  cave = list(int(input()) for _ in range(N))

  upper, lower, result = list([0]*(H+2) for _ in range(3))

  for i in range(N):
    if not i%2: lower[cave[i]+1] += 1
    else: upper[H-cave[i]] += 1

  for i in range(2,H+1): lower[i] += lower[i-1]
  for i in range(H,-1,-1): upper[i] += upper[i+1]
  for i in range(1,H+1): result[i] = upper[i] + lower[i]
  print(N-max(result), result.count(max(result)))


if __name__ == "__main__":
  N, H = map(int,input().split())
  main()