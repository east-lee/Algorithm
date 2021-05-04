def find(x):
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  global parent, number
  x,y = find(x), find(y)

  if x != y:
    parent[y] = x
    number[x] += number[y]

def main():
  global parent,number

  F = int(input())

  for _ in range(F):
    x,y = map(str,input().split())
    if x not in parent:
      parent[x] = x
      number[x] = 1
    if y not in parent:
      parent[y] = y
      number[y] = 1
    union(x,y)
    # print(parent,number)
    print(number[parent[x]])







if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    parent = {}
    number = {}
    main()