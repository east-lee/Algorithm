# 최소신장트리 연습
# 그래프이론 알고리즘
def union(a):
  global parent

  if parent[a] != a:
    parent[a] = union(parent[a])
  return parent[a]

def MST(a,b):
  global parent

  a = union(a)
  b = union(b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def main():
   result = 0
   for a,b,c in link_list:
     if union(a) != union(b):
       result += c
       MST(a,b)

   return result


def get_data():
  N, M = [int(input()) for _ in range(2)]

  link_list = []

  for _ in range(M):
    a, b, c = map(int,input().split())
    link_list.append([a,b,c])

  link_list.sort(key = lambda x:x[2])

  return [N, M, link_list]

if __name__ == "__main__":
  N, M, link_list = get_data()
  parent = [i for i in range(N+1)]
  print(main())
