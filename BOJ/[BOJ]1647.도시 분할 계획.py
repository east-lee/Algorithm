# 최소신장트리
# 크루스칼 알고리즘 사용
#

def union(a):
  global parent

  if parent[a] != a:
    parent[a] = union(parent[a])

  return parent[a]

def check_parent(a,b):
  global parent

  a = union(a)
  b = union(b)

  if a < b: parent[b] = a
  else: parent[a] = b


def main():

  total_cost = 0
  last_cost = 0
  for road in roads:
    A, B, C = road
    if union(A) != union(B):
      check_parent(A,B)
      total_cost += C
      last_cost = C

    else: continue

  return total_cost - last_cost



def get_data():
  N, M = map(int,input().split())
  roads = []

  for _ in range(M):
    A, B, C = map(int,input().split())
    roads.append([A,B,C])

  roads.sort(key=lambda x:x[2]) #유지비용순으로 정렬

  return [N,M,roads]

if __name__ == "__main__":
  N, M , roads = get_data()
  parent = [i for i in range(N+1)]
  print(main())