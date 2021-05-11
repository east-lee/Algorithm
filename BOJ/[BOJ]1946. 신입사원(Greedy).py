def main():
  N = int(input())
  scores = []

  for _ in range(N):
    scores.append(list(map(int,input().split())))

  scores.sort()
  cnt = 1
  min_interview_score = scores[0][1]

  for i in range(1,N):
    report_score, interview_score = scores[i]
    if interview_score < min_interview_score:
      cnt += 1
      min_interview_score = interview_score
  print(cnt)

if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    main()