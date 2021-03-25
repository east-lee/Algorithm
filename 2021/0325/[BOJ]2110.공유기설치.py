def solution(k,installed_cnt,min_result,last_installed,check):
  global result
  if installed_cnt == C:
    if result < min_result:
      result = min_result
    return
  elif k == N:
    return
  if min_result < result: return
  if last_installed == -1:
    solution(k+1,installed_cnt+1,min_result,house[k],check+str(house[k]))
  elif last_installed != -1 and min(min_result,house[k]-last_installed) > result:
    solution(k + 1, installed_cnt + 1, min(min_result, house[k] - last_installed), house[k], check + str(house[k]))
  solution(k+1,installed_cnt,min_result,last_installed,check)

N, C = map(int,input().split())
house = [int(input()) for _ in range(N)]
house.sort()
result = 0
solution(0,0,house[-1]-house[0],-1,'')
print(result)