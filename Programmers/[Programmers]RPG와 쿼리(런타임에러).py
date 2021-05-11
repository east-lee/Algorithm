def solution(n, z, roads, queries):
  answer = []
  dp_last = max(queries)
  value = [[] for _ in range(51)]

  for u,v,w in roads:
    value[w].append([u,v])
  dp = [-1]*(dp_last + 1)
  dp[0] = 0
  dp_pos = [[] for _ in range(dp_last + 1)] #해당쿼리에서 위치할수있는 위치의 모든 경우 들
  dp_pos[0] = [0]
  # print(value)
  for i in range(1,dp_last+1):
    dp_value = []
    dp_pos_1 = []
    dp_pos_2 = []
    for j in range(i):
      if i - j == z and dp[j] != -1:
        dp_value = [dp[j] + 1]
        dp_pos_1 = dp_pos[j]
        break
      if value[i-j] and dp[j] != -1: #차이만큼의 길이 존재한다면
        # print(i,j,'value exist')
        # print('???',dp_pos[j])
        for k in dp_pos[j]: #그전에 내가 있을 수 있는 위치가 value[i-j]의 경로에 속해있다면 dp[j]+1 and dp_pos[i]에 나머지 경로 추가
          # print('value ddd',k)
          for u,v in value[i-j]:
            if u == k:
              dp_value.append(dp[j]+1)
              dp_pos_1.append(v)
            else: #만약 그전에 있을 수 있는 위치와 출발이 다르다면 순간이동 1회 후 value[i-j] 에있는 모든 곳이 가능한 경우가 됨
              dp_value.append(dp[j] + 2)
              dp_pos_2.append(v)
    # print(i,dp_value,dp_pos_1,dp_pos_2)
    if dp_value: dp[i] = min(dp_value)
    if dp_pos_1: dp_pos[i] = dp_pos_1
    elif dp_pos_2: dp_pos[i] = dp_pos_2
  # print(dp)
  # print(dp_pos)



  answer = dp

  return answer



n = 5
# n개의 도시 / 0번 부터 n-1 번까지
z = 5

roads = [[1,2,3],[0,3,2]]
queries = [0,1,2,3,4,5,6]
print(solution(n,z,roads,queries))


# 경우의수 3개
# 연결된 도로를 따라 이동 하고 w만큼 얻음
# 안움직이고 z원 얻음
# 순간이동