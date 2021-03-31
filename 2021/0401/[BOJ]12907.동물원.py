if __name__ == "__main__":
  N = int(input())
  cnt = [0] * 41
  for i in list(map(int,input().split())):
    cnt[i] += 1
  result = -1
  if cnt[0]>2:
    result = 0

  for i in range(1,41):
    if cnt[i] > cnt[i-1]:
      result = 0
  ans = 1
  i = 0
  while cnt[i] == 2:
    ans*= 2
    i += 1
  if cnt[i] == 1:
    ans *= 2

  if not result:
    print(result)
  else:
    print(ans)
