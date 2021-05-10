from collections import deque


def solution(enroll, referral, seller, amount):
  N = len(enroll)
  answer = [0] * N
  enroll_dict = {}
  money = [[] for _ in range(N)]
  visited = [0] * N
  dq = deque()

  for i in range(N):
    enroll_dict[enroll[i]] = i

  for i in range(N):
    if referral[i] == '-': continue
    visited[enroll_dict[referral[i]]] = 1

  for i in range(N):
    if visited[i] == 0:
      dq.append(i)

  for i in range(len(seller)):
    money[enroll_dict[seller[i]]].append(amount[i] * 100)
  check = [0] * (N)
  while dq:
    people_idx = dq.popleft()
    if check[people_idx]: continue
    check[people_idx] = 1
    if referral[people_idx] == '-':
      for i in range(len(money[people_idx])):
        money[people_idx][i] -= int(money[people_idx][i] * 0.1)
      continue
    parent_idx = enroll_dict[referral[people_idx]]

    for i in range(len(money[people_idx])):
      now_money = money[people_idx][i]
      money[people_idx][i] -= int(now_money * 0.1)
      money[parent_idx].append(int(now_money * 0.1))
    dq.append(parent_idx)
    print(money, people_idx)

  for i in range(N):
    answer[i] = sum(money[i])

  return answer
solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])