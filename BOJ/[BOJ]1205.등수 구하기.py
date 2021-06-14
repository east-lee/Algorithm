def main():
  cnt = 1
  last_score =  2000000000 + 1
  for ranking in ranking_list:
    if ranking == new_score:
      return cnt
    elif last_score > new_score > ranking:
      return cnt
    else:
      last_score = ranking
      cnt += 1
  return cnt


if __name__ == "__main__":
  N, new_score, P = map(int,input().split())
  ranking_list = list()
  if N > 0:
    ranking_list = list(map(int,input().split()))

  if N==P and ranking_list[N-1] >= new_score:
    print(-1)
  else:
    print(main())
