def BFS():
  q = [V]
  new_q = []
  check_bfs = [0]*(N+1)
  check_bfs[V] = 1
  while q:
    point = q.pop()
    print(point,end=' ')
    for i in range(1,N+1):
      if check[point][i] == 1 and check_bfs[i] == 0:
        new_q.append(i)
        check_bfs[i] = 1
    if not q and new_q:
      new_q.sort(reverse=True)
      q=new_q
      new_q = []

def DFS(s,check_dfs):
  print(s,end=' ')
  for i in range(1,N+1):
    if check[s][i] == 1 and check_dfs[i] != True:
      check_dfs[i] = 1
      DFS(i,check_dfs)

if __name__ == "__main__":
  N,M,V = map(int,input().split())
  check = list([0]*(N+1) for _ in range(N+1))
  for _ in range(M):
    s,e = map(int,input().split())
    check[s][e], check[e][s] = 1,1
  check_dfs = [0 for _ in range(N+1)]
  check_dfs[V] = 1
  DFS(V,check_dfs)
  print()
  BFS()