def find_max_length():
  max_step = can_go[0]

  for i in range(len(can_go)-1):
    step = can_go[i] + can_go[i+1]
    max_step = max(max_step,step)

  return max_step

def main():
  global can_go # 한번에 갈 수 있는 길이들을 모아놓는다. => 여기서 연속된거를 두개를 골라서 가장 큰 것이 답

  step_cnt = 1
  for i in L:
    if i <= K:
      step_cnt += 1
    else:
      can_go.append(step_cnt)
      step_cnt = 1
  can_go.append(step_cnt)

  return find_max_length()


def get_data():
  N, K = map(int,input().split()) #N은 블럭의 개수 , K는 최대로 갈 수 있는 보폭
  L = list(map(int,input().split()))

  return [N,K,L]

if __name__ == "__main__":
  N, K, L = get_data()
  can_go = []
  print(main())
