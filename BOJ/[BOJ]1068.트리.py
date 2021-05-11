def main():
  global node
  visited = [0]*N
  visited[remove_node[0]] = 1
  while remove_node:
    now_remove = remove_node.pop()
    node[now_remove] = -1
    for i in range(N):
      if node[i] == now_remove and visited[i] == 0:
        remove_node.append(i)
        visited[i] = 1
        node[i] = -1

if __name__ == "__main__":
  N = int(input())
  node = list(map(int,input().split()))
  remove_node = []
  remove_node.append(int(input()))
  main()
  result = 0
  for i in range(N):
    if node[i] == -1: continue
    else:
      breaker = False
      for j in range(N):
        if i != j and node[j] == i:
          breaker = True
          break
      if not breaker: result += 1

  if result == 0 and N==2: result = 1
  print(result)