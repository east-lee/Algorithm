from collections import deque

def find_pos_change(index):
  return_list = []

  for i in [index-1,index+1,index+3,index-3]:
    if i < 0 or i >= 9: continue
    if index % 3 == 0 and i == index -1: continue
    if index % 3 == 2 and i == index + 1 : continue
    return_list.append(i)

  return return_list

def find_hole(string):
  cnt = 0
  for s in string:
    if s == "0":
      return cnt
    cnt += 1

def puzzle_to_string(arr):
  return_string = ""

  for i in range(3):
    for j in range(3):
      return_string += str(arr[i][j])

  return return_string

def string_to_puzzle(string):

  arr = list([0]*3 for _ in range(3))
  cnt = 0
  for i in range(3):
    for j in range(3):
      arr[i][j] = string[cnt]
      cnt += 1

  return arr


def main(first_string):
  global visited

  q = deque()
  q.append([first_string,0])

  while q:
    string, cnt = q.popleft()
    if string == "123456780": return cnt
    hole = find_hole(string)
    pos_change_list = find_pos_change(hole)

    for i in pos_change_list:
      new_string = list(string)[:]
      new_string[i], new_string[hole] = new_string[hole], new_string[i]
      new_string = ''.join(new_string)
      if new_string not in visited.keys():
        visited[new_string] = 1
        q.append([new_string,cnt+1])



  return -1


def get_data():
  puzzle = list(list(map(int,input().split())) for _ in range(3))

  return puzzle


if __name__ == "__main__":
  puzzle = get_data()
  visited = {}

  first_visited = puzzle_to_string(puzzle)

  visited[first_visited] = 1

  result = main(first_visited)
  print(result)
