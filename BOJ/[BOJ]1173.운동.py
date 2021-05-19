if __name__ == "__main__":
  N, m, M, T, R = map(int,input().split())
  cnt = 0
  result = 0
  now_puls = m
  if (M-m < T):
    print(-1)
  else:
    while cnt < N:
      result += 1
      if now_puls + T <= M:
        cnt += 1
        now_puls += T
      else:
        now_puls = max(now_puls-R, m)

    print(result)
