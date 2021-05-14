from collections import deque

def main():
  visited = [
    list([0]*W for _ in range(H)) for _ in range(K+1)
  ]
  visited[0][0][0] = 1

  dq = deque()
  dq.append([0,0,0,0])

  while dq:
    y,x,k,cnt = dq.popleft()
    if y==(H-1) and x==(W-1):
      return cnt

    #말처럼 움직이기
    if k<K:
      for m in range(8):
        i,j = y+horse[m][0], x+horse[m][1]
        if 0<=i<H and 0<=j<W and visited[k+1][i][j] == 0 and arr[i][j] == 0:
          visited[k+1][i][j] = 1
          dq.append([i,j,k+1,cnt+1])
    for m in range(4):
      i,j = y+monkey[m][0], x+monkey[m][1]
      if 0<=i<H and 0<=j<W and visited[k][i][j] == 0 and arr[i][j] == 0:
        visited[k][i][j] = 1
        dq.append([i,j,k,cnt+1])
  return -1


horse = [[-2,-1],[-1,-2],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]
monkey = [[-1,0],[0,1],[0,-1],[1,0]]


if __name__ == "__main__":
  K = int(input())
  W, H = map(int,input().split())
  arr = list(list(map(int,input().split())) for _ in range(H))
  print(main())