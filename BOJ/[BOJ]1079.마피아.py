def night_select(night_cnt): #밤에 마피아는 절대 안죽음
  global out_people, crime_score

  for i in range(N):
    if i == my_number or i in out_people: continue
    out_people.append(i)
    restore_list = crime_score[:]
    for j in range(N):
      if j in out_people:
        crime_score[j] = 0
      else:
        crime_score[j] += reaction[i][j]
    dfs(night_cnt+1)
    out_people.pop()
    crime_score = restore_list[:]

def morning_select(night_cnt):
  global out_people, crime_score, max_night
  max_idx = -1
  max_score = 0
  for i in range(N):
    if i in out_people: continue
    if max_score < crime_score[i]:
      max_idx = i
      max_score = crime_score[i]
  if max_idx == my_number:
    max_night = max(max_night,night_cnt)
  else:
    out_people.append(max_idx)
    dfs(night_cnt)
    out_people.pop()


def dfs(night_cnt = 0):
  # print(night_cnt,out_people,crime_score)
  if (N - len(out_people)) % 2 == 0:
    night_select(night_cnt)
  else:
    morning_select(night_cnt)


if __name__ == "__main__":
  N = int(input())
  out_people = []
  crime_score = list(map(int,input().split()))
  reaction = list(list(map(int,input().split())) for _ in range(N))
  my_number = int(input())
  max_night = 0
  dfs()
  print(max_night)