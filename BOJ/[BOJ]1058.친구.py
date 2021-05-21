from collections import deque

def main():
  max_cnt = 0

  for i in range(N):
    check_people = i
    friend = [0]*N
    friend[i] = 0
    dq = deque()
    dq.append([check_people,0])
    while dq:
      people, cnt = dq.popleft()

      if cnt == 3: break
      if friend[people]: continue

      friend[people] = 1

      for j in range(N):
        if relation[people][j] == 'Y':
          dq.append([j,cnt+1])
    max_cnt = max(max_cnt,friend.count(1) -1)

  return max_cnt


if __name__ == "__main__":
  N = int(input())
  relation = list(list(input()) for _ in range(N))
  result = main()
  print(result)