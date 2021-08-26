from collections import deque

def get_pos_degree():
  pos_degree = [False] * 360

  dq= deque()
  dq.append(0)

  while dq:

    x = dq.popleft()
    if pos_degree[x]: continue
    pos_degree[x] = True

    for i in pos_degree_list:
      a, b = x - i if x-i>=0 else x-i+360, x + i if x+i< 360 else x+i-360
      dq.append(a)
      dq.append(b)
  return pos_degree


def get_data():
  # N 만들 수 있는 각도의 개수 / K만들어야하는 각도의 개수
  N , K = map(int, input().split())
  pos_degree_list = list(map(int, input().split()))

  return [N, K, pos_degree_list]


if __name__ == "__main__":
  N, K, pos_degree_list = get_data()
  pos_degree = get_pos_degree()
  # print(pos_degree)
  for check_num in list(map(int,input().split())):
    print("YES" if pos_degree[check_num] else "NO")