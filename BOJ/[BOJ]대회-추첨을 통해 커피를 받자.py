def main():
  total_score = 0
  for i in range(len(max_scores)):
    if my_scores[i]>max_scores[i]:
      return 'hacker'
    else:
      total_score += my_scores[i]
  if total_score >=100:
    return 'draw'
  return 'none'



if __name__ == "__main__":
  max_scores = [100,100,200,200,300,300,400,400,500]
  my_scores = list(map(int,input().split()))
  print(main())