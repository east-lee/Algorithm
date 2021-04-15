def find(x):
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(s,e):
  s = find(s)
  e = find(e)

  if e<s:
    parent[s] = e
  else:parent[e] = s


if __name__ == "__main__":
  V, E = map(int,input().split())
  arr = []
  for _ in range(E):
    a,b,c = map(int,input().split())
    arr.append([c,a,b])
  arr.sort(key=lambda x:x[0])
  parent = list(i for i in range(V+1))

  result = 0

  for w,s,e in arr:
    if find(s)!=find(e):
      union(s,e)
      result += w
  print(result)
  
